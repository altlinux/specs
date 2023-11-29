
%define _unpackaged_files_terminate_build 1

Name: rpm-macros-valgrind-checkinstall
Version: 1.0
Release: alt2

Summary: Sanity check for rpm-macros-valgrind
License: MIT
Group: 	 Development/Other
Url:     https://www.altlinux.org/RPM/checkinstall


BuildRequires(pre): rpm-macros-valgrind

# make sure they cannot update rpm-macros-valgrind
# without rebuilding this package
%define get_strict_dep() %(rpmquery --qf '%%{NAME} = %%|epoch?{%%{epoch}:}|%%{version}-%%{release}%%|disttag?{:%%{disttag}}|' %1 2>/dev/null || echo '%1 = unknown')
Requires: %{get_strict_dep rpm-macros-valgrind}


%description
%summary.

%ifarch %valgrind_arches
%post
set -e
valgrind /bin/echo
%endif

%install
mkdir -p %buildroot%_libdir/%name

%files
%_libdir/%name

%changelog
* Tue Nov 28 2023 Ivan A. Melnikov <iv@altlinux.org> 1.0-alt2
- Workaround for girar noarch check

* Tue Nov 28 2023 Ivan A. Melnikov <iv@altlinux.org> 1.0-alt1
- Build for Sisyphus
