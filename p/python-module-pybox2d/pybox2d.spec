# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++ python-devel
# END SourceDeps(oneline)
# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-module-pybox2d
Version:        2.3.2
Release:        alt1.1
Summary:        A 2D rigid body simulation library for Python

Group:          Development/Python
License:        zlib
URL:            http://code.google.com/p/pybox2d/
Source0:        https://pypi.python.org/packages/cc/7b/ddb96fea1fa5b24f8929714ef483f64c33e9649e7aae066e5f5023ea426a/Box2D-%{version}.tar.gz

# Fix comments for SWIG 3.0.3 and higher
#Patch0:         pybox2d-Fix_comments_for_swig_3.0.3.patch

BuildRequires:  gcc
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  swig
Source44: import.info

%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation. Rather than paying (or begging) an animator to move your
actors around, you can let Sir Isaac Newton do the directing.

%prep
%setup -q -n Box2D-%{version}



#%patch0 -p1

# calm rpmlint down
sed -i LICENSE -e 's/\r//'

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# copy missing files
#cp library/Box2D.py %{buildroot}%{python_sitelibdir}/Box2D/

# calm rpmlint down
sed -i %{buildroot}%{python_sitelibdir}/Box2D/__init__.py -e 1d
sed -i %{buildroot}%{python_sitelibdir}/Box2D/__init__.py -e 's/\r//'

 
%files
%doc LICENSE examples/*
%{python_sitelibdir}/*


%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1.1
- applied repocop patch

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1
- automated PyPI update

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_1
- converted for ALT Linux by srpmconvert tools

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.2b2-alt1_13
- fixed build

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2b2-alt1_8
- new version

