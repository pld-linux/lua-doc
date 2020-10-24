Summary:	LuaDoc is a documentation tool for Lua source code
Summary(hu.UTF-8):	LuaDoc egy dokumentációs eszköz Lua forráskódokhoz
Summary(pl.UTF-8):	Narzędzie do dokumentowania kodu źródłowego Lua
Name:		lua-doc
Version:	3.0.1
Release:	13
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/3185/luadoc-%{version}.tar.gz
# Source0-md5:	ec3a0c0b9413e401a2d466cc0930d505
URL:		http://luaforge.net/projects/luadoc/
BuildRequires:	sed >= 4.0
Requires:	lua-filesystem
Requires:	lua-logging
Requires:	lua51
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaDoc is a documentation tool for Lua source code.

%description -l hu.UTF-8
LuaDoc egy dokumentációs eszköz Lua forráskódokhoz.

%description -l pl.UTF-8
LuaDoc jest narzędziem służącym do generowania dokumentacji na podstawie kodu
źródłowego Lua.

%prep
%setup -q -n luadoc-%{version}
%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+lua,#!%{__lua}5.1,' src/luadoc.lua.in

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
%dir %{_datadir}/lua/5.1/luadoc
%{_datadir}/lua/5.1/luadoc/*
%attr(755,root,root) %{_bindir}/luadoc
