%define  oname spnego

Name:    python3-module-%oname
Version: 0.5.4
Release: alt1

Summary: Python SPNEGO authentication library
License: MIT
Group:   Development/Python3
URL:     https://github.com/jborean93/pyspnego

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

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

%files
%doc *.md
%_bindir/pyspnego-parse
%python3_sitelibdir/%oname
%python3_sitelibdir/py%oname-%version-py%_python3_version.egg-info

%changelog
* Fri Aug 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt1
- Automatically updated to 0.5.4.

* Sat Jul 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt1
- Automatically updated to 0.5.3.

* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
