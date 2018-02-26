%def_without test
# avoid excessive dependencies
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/amazon_s3.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/monotone.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/bzr.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/cvs.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/darcs.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/mercurial.pm
%add_findreq_skiplist %perl_vendor_privlib/IkiWiki/Plugin/subversion.pm
%add_findreq_skiplist %_bindir/ikiwiki-makerepo

Name: ikiwiki
Version: 3.20110328
Release: alt1.1

Summary: A wiki compiler
License: GPLv2+
Group: Networking/WWW

Url: http://ikiwiki.info/
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-webserver-common

# Automatically added by buildreq on Sun Oct 03 2010
BuildRequires: git-core perl-CGI-FormBuilder perl-CGI-Session perl-File-chdir perl-HTML-Scrubber perl-Mail-Sendmail perl-Memoize perl-RPC-XML perl-Text-Markdown perl-TimeDate perl-XML-Simple po4a perl-devel perl-Term-ReadLine-Gnu perl-YAML

Requires: perl-Text-Markdown perl-HTML-Scrubber

%description
Ikiwiki is a wiki compiler. It converts wiki pages into HTML pages
suitable for publishing on a website. Ikiwiki stores pages and history
in a revision control system such as Subversion or Git. There are many
other features, including support for blogging, as well as a large
array of plugins.

%package w3m
Summary: Ikiwiki w3m cgi meta-wrapper
Group: Networking/WWW
Requires: w3m
Requires: %name = %version-%release

%description w3m
Enable usage of all of ikiwiki's web features (page editing, etc) in
the w3m web browser without a web server. w3m supports local CGI
scripts, and ikiwiki can be set up to run that way using the
meta-wrapper in this package.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

install -pDm0755 ikiwiki-w3m.cgi %buildroot%webserver_cgibindir/ikiwiki-w3m.cgi

%find_lang %name

%files -f %name.lang
%_bindir/ikiwiki*
%_sbindir/ikiwiki*
%_mandir/man1/ikiwiki*
%_mandir/man8/ikiwiki*
%_datadir/ikiwiki
%dir %_sysconfdir/ikiwiki
%config(noreplace) %_sysconfdir/ikiwiki/*
# contains a packlist only
%exclude %perl_vendorarch
%perl_vendorlib/IkiWiki*
%exclude %perl_vendorlib/IkiWiki*/Plugin/skeleton.pm.example
%_libexecdir/ikiwiki
%doc README debian/changelog debian/NEWS html
%doc IkiWiki/Plugin/skeleton.pm.example

%files w3m
%webserver_cgibindir/ikiwiki-w3m.cgi

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.20110328-alt1.1
- Rebuild with Python-2.7

* Wed Apr 13 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 3.20110328-alt1
- New version (fixes CVE-2011-1401).

* Mon Oct 04 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 3.20100926-alt1
- Initial build for Sisyphus.
