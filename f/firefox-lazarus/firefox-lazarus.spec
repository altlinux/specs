%define rname	lazarus
%define cid 	lazarus@interclue.com
%define ciddir  %firefox_noarch_extensionsdir/%cid

Name: firefox-lazarus
Version: 3.2
Release: alt1

Summary: Lazarus extension for Firefox
License: Freeware
Group: Networking/WWW

Url: http://lazarus.interclue.com
Source: %url/downloads/lazarus-firefox-%version.xpi
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

# these are ELF binaries for Mozilla Weave
%define _verify_elf_method skip
%brp_strip_none %ciddir
AutoReq: yes, nolib, noshell

%description
Ever had one of those "oh $*#@" moments when you realize you've
just lost half an hour of your life because something went wrong
while you were entering stuff into a web form and there doesn't
seem to be any way to recover it? If so, you need Lazarus.
If not, install it anyway, before disaster strikes!

Lazarus securely saves forms as you type, allowing you to safely
recover your lost work after server timeouts, network issues,
browser crashes, power failures, and all the other things that
can go wrong while you're entering forms, editing content,
writing webmail, etc, etc, etc...

Lazarus works on web forms, WYSIWYG editors and AJAXified forms
and will save you from almost any given server, browser,
or connection problems that might otherwise cause you to lose
your work.

Lazarus now comes with 2048-bit RSA and 256-bit AES hybrid
encryption so your data is more secure than ever! Lazarus 2.0
also includes search functionality so you can recover text even
if you can no longer find the original form you entered it into.

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -pr * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then [ ! -d "%ciddir" ] || rm -rf "%ciddir"; fi

%files
%ciddir

%changelog
* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- 3.2

* Tue Aug 09 2011 Michael Shigorin <mike@altlinux.org> 3.0.4.2-alt1
- 3.0.4.2
- autoreq += noshell (installrdf.sh)

* Tue Apr 05 2011 Michael Shigorin <mike@altlinux.org> 3.0.3-alt1
- 3.0.3 (see %url for changes)

* Sun Jan 17 2010 Michael Shigorin <mike@altlinux.org> 2.0.5-alt2
- oops, really 2.0.5

* Sun Jan 17 2010 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed Sep 02 2009 Michael Shigorin <mike@altlinux.org> 2.0.4-alt1
- 2.0.4 (see also #21236)

* Mon Jul 20 2009 Michael Shigorin <mike@altlinux.org> 2.0.3-alt2
- fixed Summary

* Fri Jul 10 2009 Michael Shigorin <mike@altlinux.org> 2.0.3-alt1
- built for ALT Linux
  + better do install it before losing another post form
