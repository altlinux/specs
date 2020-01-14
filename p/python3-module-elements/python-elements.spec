%define oname elements

Name:           python3-module-%oname
Version:        0.13
Release:        alt2

Summary:        A 2D Physics API for Python
License:        GPLv3+
Group:          Development/Python3
URL:            http://www.assembla.com/wiki/show/elements
BuildArch:      noarch

Source0:        %name-%version.tar
Source44:       import.info

Patch0:         fix-mixed-tabs-and-spaces.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 swig

Requires: python3-module-pybox2d


%description 
An easy to use API for integrating 2D physics (with pybox2d) into own\
python ideas, that includes user interfaces & simulations, as well as\
teaching & learning tools.

%prep
%setup
%patch0 -p1

# calm rpmlint down
sed -i elements/elements.py -e 1d

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
   %buildroot%python3_sitelibdir
%endif

%files
%doc LICENSE README
%python3_sitelibdir/*


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.13-alt2
- porting on python3

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_17.20100110svn
- update to new release by fcimport

* Sat Oct 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_15.20100110svn
- applied repocop patch

* Tue May 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_11.20100110svn
- converted for ALT Linux by srpmconvert tools

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_6.20100110svn
- new version

