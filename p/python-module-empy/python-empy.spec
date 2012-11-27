# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define oldname python-empy
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global tarname empy

Name:           python-module-empy
Version:        3.3
Release:        alt1_7
Summary:        A powerful and robust template system for Python

Group:          Development/Other
License:        LGPLv2+
URL:            http://www.alcyone.com/software/empy/
Source:         http://www.alcyone.com/software/%{tarname}/%{tarname}-latest.tar.gz

BuildArch:      noarch
BuildRequires:  python-module-setuptools python-devel
Source44: import.info

%description
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

%prep
%setup -q -n %{tarname}-%{version}

#fix shebang on rpmlint
sed -i -e '1d' em.py

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc COPYING README version.txt
%{python_sitelibdir_noarch}/*


%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_7
- new version; import from fc17 updates

