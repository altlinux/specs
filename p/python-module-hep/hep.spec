%define version 0.6
%define release alt10.1
Packager: Denis Medvedev <nbr@altlinux.ru>
Summary: A multiprotocol message translation server (POP,IMAP,RSS,ATOM Metaweblog)
Name: python-module-hep
Version: %version
Release: %release.1
Source: python-module-hep.tar.bz2
License: GPL
Group: Development/Python
URL: http://fettig.net/projects/hep
BuildArch: noarch

BuildPreReq: python python-module-twisted python-devel python-module-setuptools python-module-yarn
Requires: python python-module-twisted python-module-yarn
%description
Hep is a multiprotocol message server. It offers on-the-fly translation between email protocols (POP and IMAP) and web formats and protocols (RSS, Atom, and the Metaweblog API). Hep lets you read and write the Web from the comfort of your favorite email client or newreader.


%prep
%setup -n python-module-hep

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record
CFLAGS="%optflags" %__python setup.py \
        install --optimize=2 \
                --root=`pwd`/buildroot \
                --record=INSTALLED_FILES
REAL_INSTALLED=""     
for i in `cat INSTALLED_FILES`
do
 if [  -e  `pwd`/buildroot/${i/lib64/lib} ] ;
   then
   echo >/dev/null;
   else
    f=`pwd`/buildroot/${i/lib64/lib}
    d=`dirname $f`
    mkdir -p $d
    mv --force `pwd`/buildroot/$i `pwd`/buildroot/${i/lib64/lib}
   fi
 echo  ${i/lib64/lib} >>REAL_INSTALLED
done
mv REAL_INSTALLED INSTALLED_FILES

%install
mkdir %buildroot/
cp -pr buildroot/* %buildroot/
unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc README.txt LICENSE.txt



%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt10.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt10.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Denis Medvedev <nbr@altlinux.ru> 0.6-alt10
- fixed module dependencies

* Sat Apr 18 2009 Denis Medvedev <nbr@altlinux.ru> 0.6-alt9
- x86_64 noarch strange build fix

* Wed Apr 15 2009 Denis Medvedev <nbr@altlinux.ru> 0.6-alt8
- changed to noarch

* Sun Apr 12 2009 Denis Medvedev <nbr@altlinux.ru> 0.6-alt7
- renamed to python-module-hep

* Sun Nov 18 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt6
 - Removed portal reference from startup from smtp.py, because that disallowed this application to start in VE. May be smtp functionality is broken now, will test.

* Sun Nov 18 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt5
- git usage problems

* Sat Nov 17 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt4
 - Depends to python-module-twisted instead of just twisted

* Fri Nov 16 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt3
 - fixed imap

* Fri Nov 16 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt2
- some fixes about wrong imports

* Thu Nov 15 2007 Denis Medvedev <nbr@altlinux.ru> 0.6-alt1
- Initial ALT release

