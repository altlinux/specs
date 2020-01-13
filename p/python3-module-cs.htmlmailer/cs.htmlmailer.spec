%define mname cs
%define oname %mname.htmlmailer

Name: python3-module-%oname
Version: 1.0.1
Release: alt2

Summary: A library to send emails with HTML and Text mixed content
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/cs.htmlmailer/

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
Requires: python3-module-%mname = %EVR

%py3_provides %oname


%description
This small library has a method to create a MIME Multipart email object
with HTML and Text content to be able to send it by e-mail.

This allows you to prepare an HTML content (with a templating language)
and forget about the text representation of the HTML; just import the
method and call it with the HTML content and the e-mail headers (to, cc,
subject, ...)

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
    %buildroot%python3_sitelibdir/%mname/

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/__init__.py*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

