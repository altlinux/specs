%global oname testpath

Name:           python3-module-%oname
Version:        0.6.0
Release:        alt1

Summary:        Test utilities for code working with files and commands

License:        MIT
Group:          Development/Python3
URL:            https://pypi.org/project/testpath

# https://github.com/jupyter/testpath
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit
BuildRequires: python3(pytest) python3(pathlib2)
BuildRequires: python3-module-sphinx

BuildArch:      noarch

%description
Testpath is a collection of utilities for Python code working with files and
commands.

It contains functions to check things on the filesystem, and tools for
mocking system commands and recording calls to those.

%package        doc
Summary:        %name documentation
Group: Development/Documentation

%description doc
Documentation for %name.

%prep
%setup

# The exe files are not needed
rm -f %oname/*.exe

%build
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
python3 -m flit build --format wheel
# generate html docs
make SPHINXBUILD="sphinx-build-3" -C doc html

%install
pip3 install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%check
%__python3 -m pytest -v

%files
%doc README.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.dist-info

%files doc
%doc doc/_build/html

%changelog
* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0.

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Automatically updated to 0.5.0.

* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt2
- Drop python2 support.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-1
- New version 0.3.1 (#1455375)
- Uses pathlib2 instead of pathlib

* Wed Mar 08 2017 Miro Hrončok <mhroncok@redhat.com> - 0.3-1
- initial package

