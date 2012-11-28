# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define oldname python-elements
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name python-elements
%define version 0.13
# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

# Tarfile created using svn
# svn co http://svn2.assembla.com/svn/elements
# cd elements
# svn export -r %{svnrevision} . %{oldname}-%{version}
# tar -cjvf ~/%{oldname}-%{version}-%{svndate}.tar.bz2 %{oldname}-%{version}
%global svndate 20100110
%global svnrevision 230
%global tarfile %{oldname}-%{version}-%{svndate}.tar.bz2

Name:           python-module-elements
Version:        0.13
Release:        alt1_6.20100110svn
Summary:        A 2D Physics API for Python

Group:          Development/Python
License:        GPLv3+
URL:            http://www.assembla.com/wiki/show/elements
Source0:        %{tarfile}

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
Requires:       python-module-pybox2d
Source44: import.info

%description
An easy to use API for integrating 2D physics (with pybox2d) into own
python ideas, that includes user interfaces & simulations, as well as
teaching & learning tools.


%prep
%setup -q -n %{oldname}-%{version}

# calm rpmlint down
sed -i elements/elements.py -e 1d


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc CREDITS LICENSE README
%{python_sitelibdir_noarch}/*


%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_6.20100110svn
- new version

