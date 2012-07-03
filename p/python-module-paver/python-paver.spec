%define oldname python-paver
%define fedora 15
%if 0%{?fedora} < 13 || 0%{?rhel} < 6
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%define srcname Paver
Name: python-module-paver
Version: 1.0.4
Release: alt2_3
Summary: Python-based build/distribution/deployment scripting tool

Group: Development/Python
# The main paver code is licensed BSD
# The paver documentation includes jquery which is licensed MIT or GPLv2
License: BSD and (MIT or GPLv2)
URL: http://www.blueskyonmars.com/projects/paver/
Source0: http://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-devel
%if 0%{?fedora} < 13
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-module-setuptools
%endif
BuildRequires: python-module-sphinx
BuildRequires: python-module-nose

Requires:      python-module-setuptools
Source44: import.info

%description
Paver is a Python-based build/distribution/deployment scripting tool along the
lines of Make or Rake. What makes Paver unique is its integration with commonly
used Python libraries. Common tasks that were easy before remain easy. More
importantly, dealing with your applications specific needs and requirements is
now much easier.

* Build files are just Python
* One file with one syntax, pavement.py, knows how to manage your project
* File operations are unbelievably easy, thanks to the built-in version of
  Jason Orendorffa.'s path.py.
* Need to do something that takes 5 lines of code? Ita.'ll only take 5 lines of
  code..
* Completely encompasses distutils and setuptools so that you can customize
  behavior as you need to.
* Wraps Sphinx for generating documentation, and adds utilities that make it
  easier to incorporate fully tested sample code.
* Wraps Subversion for working with code that is checked out.
* Wraps virtualenv to allow you to trivially create a bootstrap script that
  gets a virtual environment up and running. This is a great way to install
  packages into a contained environment.
* Can use all of these other libraries, but requires none of them
* Easily transition from setup.py without making your users learn about or
  even install Paver! (See the Getting Started Guide for an example).


%prep
%setup -q -n %{srcname}-%{version}

# Note: This falls somewhere in between source and non-source.  It's a copy
# of the essential files from the library that's being packaged.  But it's
# zipped up.  For us, the paver command should find the uninstalled paver
# module in the directory so we might as well use it instead.
rm paver-minilib.zip

%build
%{__python} setup.py build

%check
%{__python} setup.py test

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%files
%doc LICENSE.txt README.txt
%{_bindir}/*
%{python_sitelib}/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3
- update to new release by fcimport

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt1_2.1
- Rebuild with Python-2.7

* Thu Aug 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- initial release by fcimport

