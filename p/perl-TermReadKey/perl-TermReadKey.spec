%def_without test
%define module_version 2.37
%define module_name TermReadKey
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(AutoLoader.pm) perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.37
Release: alt1.1
Summary: unknown
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
Provides: perl-Term-ReadKey = %version
Obsoletes: perl-Term-ReadKey < 2.31

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
non-blocking reads, if the architecture allows, and some generalized handy
functions for working with terminals. One of the main goals is to have the
functions as portable as possible, so you can just plug in "use
Term::ReadKey" on any architecture and have a good likelihood of it working.

Version 2.30.01:
Added handling of arrows, page up/down, home/end, insert/delete keys 
under Win32. These keys emit xterm-compatible sequences.
Works with Term::ReadLine::Perl.

=over 8

=item ReadMode MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Restore original settings.
    1    Change to cooked mode.
    2_ Change to cooked mode with echo off. 
          (Good for passwords)
    3    Change to cbreak mode.
    4    Change to raw mode.
    5    Change to ultra-raw mode. 
          (LF to CR/LF translation turned off) 
          
    Or, you may use the synonyms:
    
    restore
    normal
    noecho
    cbreak
    raw
    ultra-raw

These functions are automatically applied to the STDIN handle if no
other handle is supplied. Modes 0 and 5 have some special properties
worth mentioning: not only will mode 0 restore original settings, but it
cause the next ReadMode call to save a new set of default settings. Mode
5 is similar to mode 4, except no CR/LF translation is performed, and if
possible, parity will be disabled (only if not being used by the terminal,
however. It is no different from mode 4 under Windows.)

If you are executing another program that may be changing the terminal mode,
you will either want to say

    ReadMode 1
    system('someprogram');
    ReadMode 1;
    
which resets the settings after the program has run, or:

    $somemode=1;
    ReadMode 0;
    system('someprogram');
    ReadMode 1;
    
which records any changes the program may have made, before resetting the
mode.

=item ReadKey MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Perform a normal read using getc
    -1   Perform a non-blocked read
    >0_ Perform a timed read

(If the filehandle is not supplied, it will default to STDIN.) If there is
nothing waiting in the buffer during a non-blocked read, then undef will be
returned. Note that if the OS does not provide any known mechanism for
non-blocking reads, then a `ReadKey -1' can die with a fatal error. This
will hopefully not be common.

If MODE is greater then zero, then ReadKey will use it as a timeout value in
seconds (fractional seconds are allowed), and won't return `undef' until
that time expires. (Note, again, that some OS's may not support this timeout
behaviour.) If MODE is less then zero, then this is treated as a timeout
of zero, and thus will return immediately if no character is waiting. A MODE
of zero, however, will act like a normal getc.

There are currently some limitations with this call under Windows. It may be
possible that non-blocking reads will fail when reading repeating keys from
more then one console.

=item ReadLine MODE [, Filehandle]

Takes an integer argument, which can currently be one of the following 
values:

    0    Perform a normal read using scalar(<FileHandle>)
    -1   Perform a non-blocked read
    >0_ Perform a timed read

If there is nothing waiting in the buffer during a non-blocked read, then
undef will be returned. Note that if the OS does not provide any known
mechanism for non-blocking reads, then a `ReadLine 1' can die with a fatal
error. This will hopefully not be common. Note that a non-blocking test is
only performed for the first character in the line, not the entire line.
This call will probably not do what you assume, especially with
ReadMode's higher then 1. For example, pressing Space and then Backspace
would appear to leave you where you started, but any timeouts would now
be suspended.

This call is currently not available under Windows.

=item GetTerminalSize [Filehandle]

Returns either an empty array if this operation is unsupported, or a four
element array containing: the width of the terminal in characters, the
height of the terminal in character, the width in pixels, and the height in
pixels. (The pixel size will only be valid in some environments.)

Under Windows, this function must be called with an "output" filehandle,
such as STDOUT, or a handle opened to CONOUT$.

=item SetTerminalSize WIDTH,HEIGHT,XPIX,YPIX [, Filehandle]

Return -1 on failure, 0 otherwise. Note that this terminal size is only for
informative value, and changing the size via this mechanism will not
change the size of the screen. For example, XTerm uses a call like this when
it resizes the screen. If any of the new measurements vary from the old, the
OS will probably send a SIGWINCH signal to anything reading that tty or pty.

This call does not work under Windows.

=item GetSpeeds [, Filehandle]

Returns either an empty array if the operation is unsupported, or a two
value array containing the terminal in and out speeds, in decimal. E.g,
an in speed of 9600 baud and an out speed of 4800 baud would be returned as
(9600,4800). Note that currently the in and out speeds will always be
identical in some OS's. No speeds are reported under Windows.

=item GetControlChars [, Filehandle]

Returns an array containing key/value pairs suitable for a hash. The pairs
consist of a key, the name of the control character/signal, and the value
of that character, as a single character. This call does nothing under Windows.

Each key will be an entry from the following list:

_DISCARD
_DSUSPEND
_EOF
_EOL
_EOL2
_ERASE
_ERASEWORD
_INTERRUPT
_KILL
_MIN
_QUIT
_QUOTENEXT
_REPRINT
_START
_STATUS
_STOP
_SUSPEND
_SWITCH
_TIME

Thus, the following will always return the current interrupt character,
regardless of platform.

_%%keys = GetControlChars;
_$int = $keys{INTERRUPT};

=item SetControlChars [, Filehandle]

Takes an array containing key/value pairs, as a hash will produce. The pairs
should consist of a key that is the name of a legal control
character/signal, and the value should be either a single character, or a
number in the range 0-255. SetControlChars will die with a runtime error if
an invalid character name is passed or there is an error changing the
settings. The list of valid names is easily available via

_%%cchars = GetControlChars();
_@cnames = keys %%cchars;

This call does nothing under Windows.

=back


%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README example
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1.1
- rebuild with new perl 5.24.1

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1
- new version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1.1
- rebuild with new perl 5.20.1

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.31-alt2
- upload to Sisyphus, uses CPAN name, obsoletes perl-Term-ReadKey

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.31-alt1
- regenerated from template by package builder

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1
- initial import by package builder

