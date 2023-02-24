%define  modulename fastavro

Name:    python3-module-%modulename
Version: 1.7.2
Release: alt1

Summary: Fast Avro for Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/fastavro/fastavro

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

Source:  %name-%version.tar

%description
Apache Avro is a data serialization system. The current Python avro package is
packed with features but dog slow. fastavro is less feature complete than avro,
however it is much faster.

%prep
%setup

# Remove the already generated C files so we generate them ourselves
find fastavro/ -name "*.c" -print -delete

%build
export FASTAVRO_USE_CYTHON=1
%python3_build

%install
export FASTAVRO_USE_CYTHON=1
%python3_install

%files
%doc *.md
%_bindir/fastavro
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info

%changelog
* Fri Feb 24 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Automatically updated to 1.7.2.

* Tue Jan 31 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Automatically updated to 1.7.1.

* Thu Oct 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt1
- Automatically updated to 1.6.1.

* Wed Aug 17 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.

* Sat Jul 30 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Automatically updated to 1.5.4.

* Wed Jul 20 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.3-alt1
- Automatically updated to 1.5.3.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt1
- Automatically updated to 1.5.2.

* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Automatically updated to 1.5.1.

* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.12-alt1
- Automatically updated to 1.4.12.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.11-alt1
- Automatically updated to 1.4.11.

* Thu Mar 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.10-alt1
- Automatically updated to 1.4.10.

* Mon Jan 17 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.9-alt1
- Automatically updated to 1.4.9.

* Tue Nov 16 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.7-alt1
- Automatically updated to 1.4.7.

* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.5-alt1
- Automatically updated to 1.4.5.

* Mon Aug 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.4-alt1
- Automatically updated to 1.4.4.

* Mon Jul 19 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.3-alt1
- Automatically updated to 1.4.3.

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Automatically updated to 1.4.2.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Automatically updated to 1.4.1.

* Wed Apr 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt1
- Automatically updated to 1.3.5.

* Mon Mar 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Automatically updated to 1.3.4.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Mon Feb 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1
- Automatically updated to 1.2.4.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Automatically updated to 1.2.3.

* Thu Dec 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2.

* Thu Dec 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Tue Nov 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Wed Nov 18 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 0.23.4-alt1
- Initial build for Sisyphus.
