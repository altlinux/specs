%define module_name scripttest

Name: python3-module-%module_name
Version: 1.3
Release: alt2

Summary: Helper to test command-line scripts
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/ScriptTest/

BuildArch: noarch

Source0: %module_name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
ScriptTest is a library to help you test your interactive
command-line applications.

With it you can easily run the command (in a subprocess) and see
the output (stdout, stderr) and any file modifications.

%prep
%setup -q -n %module_name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jun 04 2017 Lenar Shakirov <snejok@altlinux.ru> 1.3-alt1
- Version 1.3
- Python3 enabled

* Sat Sep 15 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.4-alt1
- Initial release for Sisyphus (based on Fedora)
