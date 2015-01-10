Name: docx2txt
Version: 1.4
Release: alt1

Summary: Convert Docx documents to Text

License: GPLv3+
Group: Office
Url: http://docx2txt.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar

BuildArch: noarch

BuildRequires: perl

Requires: unzip

# Sent upstream by email on 2013-09-25
Patch: docx2txt-1.2-Allow-specifying-the-root-of-the-installation.patch

# Not sent upstream, the changelogs from the scripts show that it was a
# desired change on their part.
Patch1: docx2txt-1.4-Fix-the-shebang-lines.patch

%description
Command line utility to convert Docx documents to equivalent Text documents.
It supports the following features during text extraction:

 * Character conversions (" ' < & > - ... fraction and some mathematical
   symbols etc.); currency characters are converted to respective names like
   Euro.
 * Capitalisation of text blocks.
 * Center and right justification of text fitting in a line of (configurable)
   80 columns.
 * Horizontal ruler, line breaks, paragraphs separation, tabs.
 * Indicating hyperlinked text along with the hyperlink. (configurable)
 * Naive nested list formatting - assumed 8 level nesting, however you can
   handle even deeper nesting by commenting/uncommenting appropriate lines in
   Perl script.

%prep
%setup

%patch0 -p1
#patch1 -p1

%build
# Nothing to build

%install
%makeinstall_std BINDIR=%_bindir

# Fix permissions
chmod 0644 %buildroot%_sysconfdir/%name.config

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/%{name}*
%config(noreplace) %_sysconfdir/%name.config

%changelog
* Sat Jan 10 2015 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Aug 28 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 1.4-1
- Update to 1.4

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-4
- Fix the permissions on the config file.
- Fix the script shebangs to not use /usr/bin/env.

* Thu Sep 26 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-3
- Fix typo in a comment.

* Wed Sep 25 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-2
- Fix BR on Perl, as requested by Christopher.
- Properly declare the config file.

* Wed Sep 25 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-1
- Initial package for Fedora.
