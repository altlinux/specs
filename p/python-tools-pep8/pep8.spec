Name:           python-tools-pep8
Version:        0.6.0
Release:        alt2
Summary:        Python style guide checker

Group:          Development/Python

License:        MIT
URL:            https://github.com/jcrocholl/pep8

Source:        %name-%version.tar

BuildArch:      noarch
BuildRequires:  python-dev python-module-setuptools

%description
pep8 is a tool to check your Python code against some of the style conventions
in PEP 8. It has a plugin architecture, making new checks easy, and its output
is parseable, making it easy to jump to an error location in your editor.


%prep
%setup

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %buildroot

%files
%doc CHANGES.txt README.rst TODO.txt
%_bindir/pep8
%python_sitelibdir_noarch/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2
- Rebuild with Python-2.7

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1
- Initial based on Fedora spec build
