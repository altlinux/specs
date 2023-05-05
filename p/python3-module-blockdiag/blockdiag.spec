%define oname blockdiag

Name:    python3-module-%oname
Version: 3.0.0
Release: alt2

Summary: Generate block-diagram images from text

License: Apache-2.0
Group: Development/Python3
Url: http://blockdiag.com/

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-blockdiag < %EVR
Obsoletes: python-module-blockdiag < %EVR

%description
blockdiag and its family generate diagram images from simply text file.

Features:
- Generates beautiful diagram images from simple text format (similar to
  graphviz's DOT format)
- Layouts diagram elements automatically
- Embeds to many documentations; Sphinx, Trac, Redmine and some wikis

- Supports many types of diagrams
  - block diagram (with this package)
  - sequence diagram (with the seqdiag package)
  - activity diagram (with the actdiag package)
  - logical network diagram (with the nwdiag package)

Enjoy documentation with blockdiag !

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/tests

%changelog
* Fri Apr 28 2023 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt2
- NMU: Don't pack tests.

* Mon Apr 11 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Build new version.

* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus.
