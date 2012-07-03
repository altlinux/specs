%define m_distro App-Asciio
Name: perl-App-Asciio
Version: 1.02.71
Release: alt2
Summary: Plain ASCII diagram

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Graphics
License: Perl
Url: http://search.cpan.org/~nkh/App-Asciio/

BuildArch: noarch
Source: %m_distro-%version.tar
Patch0: %m_distro-%version-%release.patch
BuildRequires: perl-Term-Size perl-Data-TreeDumper perl-Data-TreeDumper-Renderer-GTK perl-Directory-Scratch perl-Directory-Scratch-Structured perl-Eval-Context perl-Module-Util perl-Test-Block perl-Test-Strict perl-Module-Build perl-Algorithm-Diff perl-Clone perl-Compress-Bzip2 perl-Data-Compare perl-File-Slurp perl-Glib perl-Gtk2 perl-List-MoreUtils perl-Readonly-XS perl-Sub-Exporter perl-Test-Exception perl-Test-NoWarnings perl-Test-Warn xvfb-run perl-unicore

Requires: perl-Term-Size

%description
This gtk2-perl application allows you to draw ASCII diagrams in a modern
(but simple) graphical application. The ASCII graphs can be saved as
ASCII or in a format that allows you to modify them later.

%prep
%setup -q -n %m_distro-%version
%patch0 -p1

%build
%def_without test
%perl_vendor_build
xvfb-run -a perl Build test

%install
%perl_vendor_install

%files
%_bindir/asciio
%perl_vendor_privlib/App/Asciio*
%doc README 

%changelog
* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02.71-alt2
- fixed test (ignoring warning message)
- fixed check with perl.req

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02.71-alt1
- initial build
