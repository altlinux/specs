
%define modname flask

Name: python-module-%modname
Version: 0.9
Release: alt2
Summary: A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

Group: Development/Python
License: BSD
URL: http://flask.pocoo.org/

BuildArch: noarch

%setup_python_module %modname

Source: Flask-%version.tar
Patch1: flask-0.9-alt-tests-in-usr-src.patch

BuildRequires: python-module-setuptools
BuildRequires: python-module-jinja2 python-module-werkzeug python-module-simplejson

%description
Flask is called a "micro-framework" because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist that
can handle that.  However Flask knows the concept of extensions that can
add this functionality into your application as if it was implemented in
Flask itself. There are currently extensions for object relational
mappers, form validation, upload handling, various open authentication
technologies and more.

%prep
%setup -n Flask-%version

%patch1 -p 1

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%check
%__python ./setup.py test

%files -f INSTALLED_FILES
%doc AUTHORS README LICENSE
%exclude %python_sitelibdir_noarch/flask/testsuite

%changelog
* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2
- Don't package testsuite.

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt1
- Initial build for Sisyphus.

