%define _unpackaged_files_terminate_build 1

Name: abcmidi
Version: 2026.06.16
Release: alt1

Summary: Converter from ABC to MIDI format and back
License: GPL-2.0
Group: Sound
Url: https://github.com/sshlien/abcmidi

Source: %name-%version.tar

%description
This package contains the programs `abc2midi' and `midi2abc',  which
convert from the abc musical notation format to standard MIDI format
and vice-versa. They can generate accompaniment from guitar chords
in the abc file, as well as insert various MIDI events; the
MIDI-to-abc translation tries to figure out bars, triplets and
accidentals on its own.

The package also contains `abc2abc' (an abc prettyprinter/transposer),
`mftext' (a program that dumps a MIDI file as text), and `midicopy'
(a program that extracts specific tracks, channels or time intervals
from a MIDI file).

The package also contains Yet another ABC to PostScript converter (yaps)
which translates tunes written in the ABC format to PostScript,
which can then be viewed on screen or printed. It is essentially a
(non-exclusive) alternative to abc2ps, being based on the abc2ps
PostScript code together with the ABC parser from the abcmidi package.

%prep
%setup

%build
%add_optflags -std=gnu17
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md doc/{abcguide.txt,abcmatch.txt,history.txt,hudsonshift.txt,readme.txt,yapshelp.txt} samples
%_bindir/*
%_man1dir/*
%exclude %_datadir/doc/%name

%changelog
* Wed Jun 17 2026 Nikolay Strelkov <snk@altlinux.org> 2026.06.16-alt1
- New version 2026.06.16.

* Mon Jun 08 2026 Nikolay Strelkov <snk@altlinux.org> 2026.06.06-alt1
- New version 2026.06.06.

* Mon Jun 01 2026 Nikolay Strelkov <snk@altlinux.org> 2026.05.31-alt1
- New version 2026.05.31.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 2026.04.26-alt1
- New version 2026.04.26.

* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 2026.02.24-alt2
- Fixed FTBFS caused by gcc15.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 2026.02.24-alt1
- New version 2026.02.24.

* Sat Feb 14 2026 Nikolay Strelkov <snk@altlinux.org> 2026.02.13-alt1
- New version 2026.02.13.

* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 2025.11.26-alt1
- New version 2025.11.26.

* Thu Jul 03 2025 Nikolay Strelkov <snk@altlinux.org> 2025.06.27-alt1
- Initial build for Sisyphus
