# vim: set ft=spec: -*- rpm-spec -*-

%define modulename sekizai

Name: python-module-django-%modulename
Version: 0.7
Release: alt3.1

%setup_python_module %modulename

Summary: Django Template Blocks with extra functionality
License: %bsd
Group: Development/Python

Url: http://django-sekizai.readthedocs.org/
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# git://github.com/ojii/django-sekizai.git
Source: %name-%version.tar

Requires: Django >= 1.2.7
# see setup.py
Requires: python-module-django-classy-tags >= 0.3.1

BuildPreReq: rpm-build-licenses
BuildPreReq: Django >= 1.2.7
BuildPreReq: python-module-django-tests
BuildPreReq: python-module-django-dbbackend-sqlite3 >= 1.2.7
BuildPreReq: python-module-django-classy-tags >= 0.3.1
BuildPreReq: python-module-setupdocs
BuildPreReq: python-module-sphinx

%description
Sekizai means "blocks" in Japanese, and that's what this app provides.
A fresh look at blocks. With django-sekizai you can define placeholders
where your blocks get rendered and at different places in your templates
append to those blocks. This is especially useful for css and javascript.
Your subtemplates can now define css and javscript files to be included,
and the css will be nicely put at the top and the javascript to the
bottom, just like you should. Also sekizai will ignore any duplicate
content in a single block.

%prep
%setup

%build
%python_build

# doc
pushd docs
make html
popd

%install
%python_install

%check
python runtests.py

%files
%doc LICENSE README.rst docs/_build
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt3.1
- Fix build requires.

* Tue Apr 02 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt3
- Fix build requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt2
- Fix requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux Sisyphus
