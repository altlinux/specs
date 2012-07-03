%define module_name mongoengine

Name: python-module-%module_name
Version: 0.6.2
Release: alt1
Summary: A Python Document-Object Mapper for working with MongoDB

License: MIT
Group: Development/Python
Url: http://hmarr.com/mongoengine/

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel python-module-distribute

%description
MongoEngine is a Python Object-Document Mapper for working with MongoDB.
MongoEngine is an ORM-like layer on top of PyMongo.

%prep
%setup -q

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/tests

%files
%python_sitelibdir/%module_name
%exclude %python_sitelibdir/*.egg-*

%changelog
* Thu Jun 21 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Nov 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

