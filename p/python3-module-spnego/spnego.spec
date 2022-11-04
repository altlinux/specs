%define  oname spnego

%def_with check

Name:    python3-module-%oname
Version: 0.6.3
Release: alt1

Summary: Python SPNEGO authentication library

License: MIT
Group:   Development/Python3
URL:     https://github.com/jborean93/pyspnego

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-pytest-mock
%endif

# This is stuff for windows OS
%add_python3_req_skip spnego._sspi_raw.sspi

BuildArch: noarch

Source:  %name-%version.tar

%description
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.md
%_bindir/pyspnego-parse
%python3_sitelibdir/%oname
%python3_sitelibdir/py%oname-%version-py%_python3_version.egg-info

%changelog
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
