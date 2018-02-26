%define subname mrim
%define cname jabber-mrim
%define username _jabber_%subname
%define	svn	20080618
Summary: Mail.ruIM-transport for jabber servers
Name: jabber-mrim
Version: 0.2
Release: alt1.svn%svn.1.qa1.1
License: GPL
Group: System/Servers
URL: http://svn.xmpp.ru/repos/mrim/
Packager: Mikhail Pokidko <pma@altlinux.org>
Requires: python-module-xmpp >= 0.3.1, jabber-common
BuildRequires: jabber-common
Source0: %subname-%version.svn%svn.tar.gz
Source1: %subname.init
Source2: %subname.conf
Source3: %subname.adapter
Patch0: %subname.patch
Patch1: %subname.utf.alt.patch
BuildArch: noarch
Obsoletes: ejabberd-mrim, jabberd2-mrim

%description
Mrim is an Open Source (GPL) XMPP to Mail.ru-IM Transport (aka M-Agent).
It is written in Python and built on top of xmpp.py library (http://xmpppy.sourceforge.net).

%prep
%setup -q -n %subname
#patch0 -p1
%patch1 -p1

%build

%install
mkdir -p %buildroot%_datadir/%cname \
	%buildroot%_initdir \
	%buildroot%_sysconfdir/%cname \
	%buildroot%_logdir/%cname \
	%buildroot%_spooldir/%cname \
	%buildroot/var/run/%cname
	#buildroot%_sysconfdir/%cname/%subname.cfg \
	
	
cp -r ./*  %buildroot%_datadir/%cname/
#cp mrim.conf.example %buildroot%_sysconfdir/%cname/%subname.conf
install -pD -m0755 %SOURCE1 %buildroot%_initdir/%cname
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/%cname/%subname.conf
install -pD -m0755 %SOURCE3 %buildroot%_jabber_component_dir/%subname

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%pre
%_sbindir/groupadd -r -f %username 2>/dev/null ||:
%_sbindir/useradd -r -g %username -c 'jabber transport' -d %_datadir/%cname \
 -s /dev/null %username 2>/dev/null ||:


%post
%_jabber_config
%post_service %name

%files
%doc COPYING ChangeLog INSTALL README TODO
%_jabber_component_dir/%subname
%config(noreplace) %_sysconfdir/%cname/*
%attr(0755,%username,%username) %_logdir/%cname/
%attr(0755,%username,%username) %_spooldir/%cname/
%attr(0755,%username,%username) /var/run/%cname/
%_initdir/*
%_datadir/%cname/*


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.svn20080618.1.qa1.1
- Rebuild with Python-2.7

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.2-alt1.svn20080618.1.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for jabber-mrim
  * postclean-05-filetriggers for spec file

* Wed Dec 02 2008 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20080618.1
- Rebuilt with python 2.6

* Wed Jun 18 2008 Mikhail Pokidko <pma@altlinux.org> 0.2-alt1.svn20080618
- Fixed #16083

* Tue Apr 29 2008 Mikhail Pokidko <pma@altlinux.org> 0.2-alt1.svn20080429
- Fresh svn version. Fixed #11367, #14844, #15446

* Tue Mar 27 2007 Mikhail Pokidko <pma@altlinux.ru> 0.1.1-alt1
- ALT Linux Jabber Policy package.
- ejabberd-mrim (pma@) and jabberd2-mrim (alexsid@) merge.


