Name: git-merge-changelog
Version: %{get_version gnulib}
Release: alt1

Summary: git merge driver for GNU style ChangeLog files
License: GPLv2+
Group: Text tools
Url: http://www.gnu.org/software/gnulib/
BuildRequires(pre): gnulib

%description
The default merge driver of 'git' *always* produces conflicts when
pulling public modifications into a privately modified ChangeLog file.
This is because ChangeLog files are always modified at the top; the
default merge driver has no clue how to deal with this. Furthermore
the conflicts are presented with more <<<< ==== >>>> markers than
necessary; this is because the default merge driver makes pointless
efforts to look at the individual line changes inside a ChangeLog entry.

git-merge-changelog program serves as a 'git' merge driver that avoids
these problems.
1. It produces no conflict when ChangeLog entries have been inserted
   at the top both in the public and in the private modification. It
   puts the privately added entries above the publicly added entries.
2. It respects the structure of ChangeLog files: entries are not split
   into lines but kept together.
3. It also handles the case of small modifications of past ChangeLog
   entries, or of removed ChangeLog entries: they are merged as one
   would expect it.
4. Conflicts are presented at the top of the file, rather than where
   they occurred, so that the user will see them immediately. (Unlike
   for source code written in some programming language, conflict markers
   that are located several hundreds lines from the top will not cause
   any syntax error and therefore would be likely to remain unnoticed.)

%prep
%setup -cT

%build
gnulib-tool --create-testdir --dir=$PWD %name
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*

%changelog
* Wed Apr 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.7312.7995834-alt1
- Rebuilt with gnulib snapshot v0.0-7312-g7995834.

* Wed Jan 11 2012 Dmitry V. Levin <ldv@altlinux.org> 0.0.6780.bfacc22-alt1
- Rebuilt with gnulib snapshot v0.0-6780-gbfacc22.

* Thu Sep 15 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6125.da1717b-alt1
- Rebuilt with gnulib snapshot v0.0-6125-gda1717b.

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.5864.0f247f9-alt1
- Rebuilt with gnulib snapshot v0.0-5864-g0f247f9.

* Fri Jan 07 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.4800.a036b76-alt1
- Gnulib snapshot v0.0-4800-ga036b76.
