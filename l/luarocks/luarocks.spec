%define luaver 5.1
%define download_helper curl

Name: luarocks
Version: 2.1.2
Release: alt1

Summary: A deployment and management system for Lua modules
License: MIT
Group: Development/Tools
Url: http://luarocks.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lua5 %download_helper

BuildRequires: liblua5-devel >= %luaver
BuildRequires: lua5 >= %luaver
BuildRequires: %download_helper

BuildArch: noarch

%description
LuaRocks allows you to install Lua modules as self-contained packages
called "rocks", which also contain version dependency
information. This information is used both during installation, so
that when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module is required, the
correct version is loaded. LuaRocks supports both local and remote
repositories, and multiple local rocks trees.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=%{_prefix} \
            --lua-version=%{luaver} \
            --with-lua-dir=%{_datadir}/lua5 \
            --with-downloader=%download_helper
%make_build

%install
%make DESTDIR=%buildroot install 
        
# fix symlinks to versioned binaries
for f in luarocks{,-admin};
do
  mv -f $RPM_BUILD_ROOT%{_bindir}/$f{-%{luaver},}
done


%files
%doc COPYING* README.md
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config-%{luaver}.lua
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%_datadir/lua5/luarocks

%changelog
* Fri Jul 4 2014 Vladimir Didenko <cow@altlinux.org> 2.1.2-alt1
- new version

* Sat Aug 31 2013 Vladimir Didenko <cow@altlinux.org> 2.1.0-alt1
- Initial build
