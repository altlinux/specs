Name: cvsweb
Version: 3.0.6
Release: alt1
Summary: Web interface for CVS repositories

License: BSD
Group: System/Servers
Url: http://www.freebsd.org/projects/cvsweb.html
Source: http://people.freebsd.org/~scop/cvsweb/cvsweb-%version.tar.gz
Patch: cvsweb-fedora-config.patch
Requires: rcs
BuildArch: noarch


# TODO: add runtime reqs for String::Ediff, MIME::Types, Compress::Zlib
# Automatically added by buildreq on Mon Sep 26 2005 (-bi)
BuildRequires: perl-Compress-Zlib perl-IPC-Run perl-URI

%description
CVSweb is a WWW interface for CVS repositories with which you can
browse a file hierarchy on your browser to view each file's revision
history in a very handy manner. This package contains the FreeBSD
version of CVSweb.

%prep
%setup -q
%patch -p1

%build

%install
install -pD -m755 cvsweb.cgi $RPM_BUILD_ROOT/var/www/cgi-bin/cvsweb.cgi
install -pD -m644 cvsweb.conf $RPM_BUILD_ROOT%_sysconfdir/cvsweb/cvsweb.conf

install -pD -m644 css/cvsweb.css $RPM_BUILD_ROOT/var/www/html/css/cvsweb.css

install -d $RPM_BUILD_ROOT%_sysconfdir/cvsweb/conf.d

install -d $RPM_BUILD_ROOT%_datadir/enscript/hl
install -p -m644 enscript/lang_cvsweb*.st $RPM_BUILD_ROOT%_datadir/enscript/hl

install -pD -m644 icons/minigraph.png $RPM_BUILD_ROOT/var/www/icons/small/minigraph.png

%files
%doc INSTALL README TODO
%dir %_sysconfdir/cvsweb
%config(noreplace) %_sysconfdir/cvsweb/cvsweb.conf
%dir %_sysconfdir/cvsweb/conf.d
/var/www/cgi-bin/cvsweb.cgi
/var/www/html/css
/var/www/icons/small/minigraph.png
%_datadir/enscript/

%changelog
* Mon Sep 26 2005 Victor Forsyuk <force@altlinux.ru> 3.0.6-alt1
- 3.0.6.

* Wed Jun 08 2005 Victor Forsyuk <force@altlinux.ru> 3.0.5-alt1
- New version.

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 1.112-alt2
- rebuild

* Sat Jan 05 2002 Rider <rider@altlinux.ru> 1.112-alt1
- 1.112
- spec cleanup
- russian summary and description

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Jan  4 2001 Frederic Lepied <flepied@mandrakesoft.com> 1.93-3mdk
- added requires rcs
- fix bad config file path

* Mon Sep 25 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.93-2mdk
- /home/httpd => /var/www

* Wed Aug 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.93-1mdk
- 1.93

* Fri Jul 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.89-1mdk
- 1.89 (security fix).

* Wed Apr 19 2000 dam's <damien@mandrakesoft.com> 1.80-2mdk
- changed icon.

* Tue Mar  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.80-1mdk
- mandrake version.

* Tue Oct 12 1999 Peter Hanecak <hanecak@megaloman.sk>
- initial spec (based on Ryan Weaver's <ryanw@infohwy.com> gtksee spec
  because i like the style of it)
