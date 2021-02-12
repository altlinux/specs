%define target_lua_version 5.1

# Original package name cqueues
%define oname cqueues
%define ver 20200726
%define oversion %ver.51-0
%define rockspec cqueues-%oversion.rockspec

Name: lua%target_lua_version-module-%oname
Version: %ver
Release: alt1
Summary: Continuation Queues
License: MIT
Group: Development/Other
Url: http://25thandclement.com/~william/projects/cqueues.html
Provides: luarocks%target_lua_version(%oname) = %EVR

%if "%target_lua_version" == "5.3"
Obsoletes: lua-module-%oname < %EVR
Provides: lua-module-%oname = %version
%else
Obsoletes: lua5-%oname < %EVR
Provides: lua5-%oname = %version
%endif

Source: https://github.com/wahern/cqueues/archive/cqueues-rel-%ver.tar.gz
Source1: https://luarocks.org/manifests/daurnimator/%rockspec

BuildRequires(pre): rpm-macros-lua >= 1.4
BuildRequires: liblua%target_lua_version-devel lua%target_lua_version-luarocks
BuildRequires: libssl-devel

%add_findreq_skiplist %luarocks_dbdir/%oname/*/*/*

%description
Continuation Queues:
Embeddable asynchronous networking, threading, and notification framework for Lua on Unix.

%prep
%setup -n %oname-rel-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc LICENSE* README* docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Fri Feb 12 2021 Alexey Shabalin <shaba@altlinux.org> 20200726-alt1
- Update to 20200726

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 20190813-alt1
- Initial build
