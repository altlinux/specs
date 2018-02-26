%define emacs_sitestart_d  %{_datadir}/emacs/site-lisp/site-start.d
%define xemacs_sitestart_d %{_datadir}/xemacs/site-packages/lisp/site-start.d

Name:           rpmdevtools
Version:        6.4
Release: alt1.1.1.1
Summary:        RPM Development Tools from Fedora Project.

Group:          Development/Other
# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:        GPLv2+ and GPLv2
URL:            http://fedoraproject.org/
Source0:        %{name}-%{version}.tar.bz2

BuildArch:      noarch
# Minimal RPM build requirements
Requires:       bash
Requires:       bzip2
Requires:       coreutils
Requires:       cpio
Requires:       diffutils
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       gcc-c++
Requires:       grep
Requires:       gzip
Requires:       info
Requires:       make
Requires:       patch
Requires:       rpm-build
Requires:       sed
Requires:       tar
Requires:       unzip
Requires:       util-linux
Requires:       which
# Additionally required for tool operations
#Requires:      cpio
Requires:       fakeroot
Requires:       file
Requires:       perl
Requires:       python
Requires:       rpm-python
#Requires:      sed
Requires:       wget

###########################
# removed/split components:
Requires: qa-robot
Requires: spectool
%add_findreq_skiplist /usr/share/rpmdevtools/*
Packager: Igor Vlasenko <viy@altlinux.org>
###########################


%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5          Display the md5sum of all files in an RPM
rpmdev-vercmp       RPM version comparison checker
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
...and many more.


%prep
%setup -q

%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# for dir in %{emacs_sitestart_d} %{xemacs_sitestart_d} ; do
#   install -dm 755 $RPM_BUILD_ROOT$dir
#   ln -s %{_datadir}/rpmdevtools/rpmdev-init.el $RPM_BUILD_ROOT$dir
#   touch $RPM_BUILD_ROOT$dir/rpmdev-init.elc
# done

# %triggerin -- emacs-common
# [ -d %{emacs_sitestart_d} ] && \
#   ln -sf %{_datadir}/rpmdevtools/rpmdev-init.el %{emacs_sitestart_d} || :

# %triggerin -- xemacs-common
# [ -d %{xemacs_sitestart_d} ] && \
#   ln -sf %{_datadir}/rpmdevtools/rpmdev-init.el %{xemacs_sitestart_d} || :

# %triggerun -- emacs-common
# [ $2 -eq 0 ] && rm -f %{emacs_sitestart_d}/rpmdev-init.el* || :

# %triggerun -- xemacs-common
# [ $2 -eq 0 ] && rm -f %{xemacs_sitestart_d}/rpmdev-init.el* || :


%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_datadir}/rpmdevtools/
%{_bindir}/rpm*
#%ghost %{_datadir}/*emacs
%{_mandir}/man[18]/rpm*.[18]*


%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.4-alt1.1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.4-alt1.1.1
- Rebuilt with python 2.6

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 6.4-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 05 2007 Igor Vlasenko <viy@altlinux.ru> 6.4-alt1
- first build for ALT Linux;
- removed included at@' qa-robot :)
- spectool is built in a separate source;
- added dependency on qa-robot and spectool.
- TODO: emacs and xemacs.

