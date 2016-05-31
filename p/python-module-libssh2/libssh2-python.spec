# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)
%define oldname libssh2-python
%{!?python_sitearch: %define python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Python binding for the libssh2 library
Name: python-module-libssh2
Version: 0.7.1
Release: alt1_11
License: LGPLv2+
Group: Development/C
URL: https://github.com/wallunit/ssh4py
# The source for the package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://github.com/wallunit/ssh4py.git
#  cd ssh4py ; python setup.py sdist
Source0: https://github.com/wallunit/ssh4py/zipball/0.7.1/%{oldname}-%{version}.tar.gz

BuildRequires: python-dev
BuildRequires: libssh2-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
Source44: import.info

%description
libssh2-python is a python binding for the libssh2 library


%prep
%setup -n %{oldname}-%{version} -q


%build
python setup.py build


%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT


%files
%doc README.txt COPYING
%{python_sitelibdir}/libssh2.so
%{python_sitelibdir}/libssh2*-*.egg-info

%changelog
* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_11
- converted for ALT Linux by srpmconvert tools

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1_3.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_3
- initial import by fcimport

