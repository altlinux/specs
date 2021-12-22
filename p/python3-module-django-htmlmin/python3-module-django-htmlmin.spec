%define _unpackaged_files_terminate_build 1
%define oname django-htmlmin

%def_with check

Name: python3-module-%oname
Version: 0.11.0
Release: alt0.git.01575db

Summary: HTML minifier for Python frameworks (not only Django, despite the name).
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/cobrateam/django-htmlmin
BuildArch: noarch

# VCS:https://github.com/cobrateam/django-htmlmin
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-beautifulsoup4

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-six
BuildRequires: python3-module-mock
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
django-html is an HTML minifier for Python, with full support for HTML 5.
It supports Django, Flask and many other Python web frameworks.
It also provides a command line tool, that can be used for static websites
or deployment scripts.

%prep
%setup
%patch0 -p1

sed -i "s/from \.util import force\_text/from htmlmin\.util import force\_text/g" htmlmin/minify.py

%build
%python3_build_debug

%install
%python3_install

%check
find . -name "*.pyc" -delete
python3 -m django test --settings htmlmin.tests.mock_settings htmlmin


%files
%doc *.rst AUTHORS LICENSE
%python3_sitelibdir/*
%_bindir/pyminify

%changelog
* Tue Dec 21 2021 Dmitry Lyalyaev <fruktime@altlinux.org> 0.11.0-alt0.git.01575db
- Initial build for ALT Linux


