Summary:	LuaDoc is a documentation tool for Lua source code
Summary(hu.UTF-8):	LuaDoc egy dokumentációs eszköz Lua forráskódokhoz
Summary(pl.UTF-8):	Narzędzie do dokumentowania kodu źródłowego Lua
Name:		lua-doc
Version:	3.0.1
Release:	7
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/3185/luadoc-%{version}.tar.gz
# Source0-md5:	ec3a0c0b9413e401a2d466cc0930d505
URL:		http://luaforge.net/projects/luadoc/
BuildRequires:	sed >= 4.0
Requires:	lua-filesystem
Requires:	lua-logging
Requires:	/usr/bin/lua
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaDoc is a documentation tool for Lua source code.

%description -l hu.UTF-8
LuaDoc egy dokumentációs eszköz Lua forráskódokhoz.

%description -l pl.UTF-8
LuaDoc jest narzędziem służącym do generowania dokumentacji
na podstawie kodu źródłowego Lua.

%prep
%setup -q -n luadoc-%{version}

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+lua(\s|$),#!%{__lua},' src/luadoc.lua.in

%build

%install
rm -rf $RPM_BUILD_ROOT

VERSION=$(echo 'print(_VERSION)' | %{__lua} | %{__sed} 's|Lua \(.*\)|\1|')

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LUA_LIBDIR=$RPM_BUILD_ROOT%{_libdir}/lua/$VERSION \
	LUA_DIR=$RPM_BUILD_ROOT%{_datadir}/lua/$VERSION \
	SYS_BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LUA_INTERPRETER=%{__lua}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
%dir %{_datadir}/lua/*/luadoc
%{_datadir}/lua/*/luadoc/*
%attr(755,root,root) %{_bindir}/luadoc
