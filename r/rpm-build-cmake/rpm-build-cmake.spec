Name: rpm-build-cmake
Version: 4.0.0
Release: alt1

Summary: RPM build enviroment for building RPM packages using cmake

License: BSD
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3

Requires: cmake >= %version

Requires: rpm-macros-cmake = %EVR

%description
RPM build enviroment for packaging applications that use cmake.

%package -n rpm-macros-cmake
Summary: Set of RPM macros for packaging applications that use cmake
Group: Development/Other
Conflicts: cmake = 2.8.0-alt1
Conflicts: rpm-build-compat <= 1.5.1-alt1

%description -n rpm-macros-cmake
Set of RPM macros for packaging applications that use cmake.

%prep
%setup

%install
install -D -m644 cmake.macros %buildroot/%_rpmmacrosdir/cmake
install -D -m755 cmake.prov %buildroot%_libexecdir/rpm/cmake.prov
install -D -m755 cmake.prov.files %buildroot%_libexecdir/rpm/cmake.prov.files

%files
/usr/lib/rpm/cmake.prov
/usr/lib/rpm/cmake.prov.files

%files -n rpm-macros-cmake
%_rpmmacrosdir/cmake

%changelog
* Mon Apr 07 2025 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- apply -DCMAKE_POLICY_VERSION_MINIMUM=3.5

* Sat Apr 06 2024 Vitaly Lipatov <lav@altlinux.ru> 3.29.1-alt1
- build as a standalone package
