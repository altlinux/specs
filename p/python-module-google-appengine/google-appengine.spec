%define mname google
%define oname %mname-appengine

%def_with python3

Name: python-module-%oname
Version: 1.9.15
Release: alt1.svn20141104
Summary: Run your web applications on Google's infrastructure
License: ASLv2.0
Group: Development/Python
Url: https://cloud.google.com/appengine/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://googleappengine.googlecode.com/svn/trunk/python/
Source: %name-%version.tar

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%mname
%py_provides %mname.appengine
%add_python_req_skip appengine_pipeline google3

%description
Google App Engine lets you build and run applications on Google's
infrastructure. App Engine applications are easy to create, easy to
maintain, and easy to scale as your traffic and data storage needs
change. With App Engine, there are no servers for you to maintain. You
simply upload your application and it's ready to go.

%if_with python3
%package -n python3-module-%oname
Summary: Run your web applications on Google's infrastructure
Group: Development/Python3
Requires: python3-module-%mname
%py3_provides %mname.appengine
%add_python3_req_skip appengine_pipeline google3 toaiff sunaudio rfc822
%add_python3_req_skip stringtemplate3 stringold statvfs sha sets popen2
%add_python3_req_skip new neo_util neo_cs mutex multifile mimetools
%add_python3_req_skip mhlib md5 imputil htmllib hotshot fpformat
%add_python3_req_skip dircache audiodev UserDict MimeWriter Bastion
%add_findreq_skiplist %python3_sitelibdir/%mname/appengine/_internal/django/utils/simplejson/encoder.py

%description -n python3-module-%oname
Google App Engine lets you build and run applications on Google's
infrastructure. App Engine applications are easy to create, easy to
maintain, and easy to scale as your traffic and data storage needs
change. With App Engine, there are no servers for you to maintain. You
simply upload your application and it's ready to go.
%endif

%prep
%setup

sed -i '/#!\/usr\/bin.*/d' $(find %mname -type f -name '*.py')

%if_with python3
cp -fR . ../python3
find ../python3/%mname -type f -name '*.py' -exec 2to3 -w -n '{}' +
find ../python3/lib/fancy_urllib -type f -name '*.py' \
	-exec 2to3 -w -n '{}' +
%endif

%install
install -d %buildroot%python_sitelibdir
cp -fR %mname %buildroot%python_sitelibdir/
cp -fR lib/fancy_urllib %buildroot%python_sitelibdir/
rm -f %buildroot%python_sitelibdir/%mname/__init__.py
install -d %buildroot%_bindir
install -p -m755 appcfg.py %buildroot%_bindir/

%if_with python3
pushd ../python3
install -d %buildroot%python3_sitelibdir
cp -fR %mname %buildroot%python3_sitelibdir/
cp -fR lib/fancy_urllib %buildroot%python3_sitelibdir/
rm -f %buildroot%python3_sitelibdir/%mname/__init__.py
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' appcfg.py
install -p -m755 appcfg.py %buildroot%_bindir/appcfg.py3
popd
%endif

%files
%doc BUGS README RELEASE_NOTES new_project_template demos/python/guestbook
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc BUGS README RELEASE_NOTES new_project_template demos/python/guestbook
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt1.svn20141104
- Initial build for Sisyphus

