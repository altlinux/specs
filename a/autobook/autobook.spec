Name: autobook
Version: 1.5
Release: alt2

Summary: The Autoconf, Automake, and Libtool book
License: OPL
Group: Books/Computer books
Url: http://sourceware.org/%name
BuildArch: noarch

Source0: %url/%name-%version.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

%description
What is "it"?  The GNU Autotools, a group of utilities developed in
the 1990s for the GNU Project.  The authors of this book and I were
some of its principal developers, but it turned out to help solve many
other peoples' problems as well, and many other people contributed to it.
It is one of the many projects that developed by cooperation while making
what is now often called GNU/Linux.  The community made the GNU Autotools
widespread, as people adopted it for their own programs and extended it
where they found that was needed.  The creation of Libtool is that type
of contribution.
 
Autoconf, Automake, and Libtool were developed separately, to make
tackling the problem of software configuration more manageable by
partitioning it.  But they were designed to be used as a system, and
they make more sense when you have documentation for the whole system.
This book stands a level above the software packages, giving the
expertise of its authors in using this whole system to its fullest.
It was written by people who have lived closest to the problems and
their solutions in software.

%prep
%setup -q
ln -s %name.html index.html

%files
%doc --no-dereference *

%changelog
* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.5-alt2
- add Packager tag to spec file

* Tue May 01 2007 Igor Zubkov <icesik@altlinux.org> 1.5-alt1
- 1.4 -> 1.5

* Mon Aug 08 2005 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Updated to 1.4

* Fri Sep 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3-alt1
- 1.3

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 1.2-ipl1
- Initial revision.
