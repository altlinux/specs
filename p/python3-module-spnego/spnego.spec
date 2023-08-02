%define  oname spnego

%def_with check

Name:    python3-module-%oname
Version: 0.9.1
Release: alt2

Summary: Python SPNEGO authentication library

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pyspnego
VCS:     https://github.com/jborean93/pyspnego

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-pytest-mock
%endif

# This is stuff for windows OS
%add_python3_req_skip spnego._sspi_raw.sspi

%description
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%_bindir/pyspnego-parse
%python3_sitelibdir/%oname
%python3_sitelibdir/py%oname-%version.dist-info

%changelog
* Wed Aug 02 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt2
- Moved on modern pyproject macros.

* Wed Jun 14 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt1
- Automatically updated to 0.9.1.

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Automatically updated to 0.9.0.

* Fri Feb 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Automatically updated to 0.8.0.

* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Automatically updated to 0.7.0.

* Fri Nov 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Automatically updated to 0.6.3.

* Thu Oct 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.2-alt1
- Automatically updated to 0.6.2.

* Wed Oct 26 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Automatically updated to 0.6.1.

* Thu Aug 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0.
- Build with check.

* Fri Aug 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt1
- Automatically updated to 0.5.4.

* Sat Jul 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt1
- Automatically updated to 0.5.3.

* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
