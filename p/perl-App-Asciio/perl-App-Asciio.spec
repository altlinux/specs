# BEGIN SourceDeps(oneline):
BuildRequires: perl(Clone.pm) perl(Compress/Bzip2.pm) perl(Data/TreeDumper.pm) perl(Data/TreeDumper/Renderer/GTK.pm) perl(Encode.pm) perl(Eval/Context.pm) perl(File/HomeDir.pm) perl(File/Slurp.pm) perl(Glib.pm) perl(Gtk3.pm) perl(Gtk3/Helper.pm) perl(HTTP/Daemon.pm) perl(HTTP/Request/Params.pm) perl(HTTP/Status.pm) perl(HTTP/Tiny.pm) perl(Hash/Slice.pm) perl(Heap/Binomial.pm) perl(Heap/Elem.pm) perl(IO/Prompter.pm) perl(JSON.pm) perl(List/MoreUtils.pm) perl(Memoize.pm) perl(Module/Build.pm) perl(Module/Build/Compat.pm) perl(Module/Util.pm) perl(Pango.pm) perl(Readonly.pm) perl(Sereal.pm) perl(Sereal/Encoder.pm) perl(Sub/Exporter.pm) perl(Term/ANSIColor.pm) perl(Term/ReadKey.pm) perl(Term/Size/Any.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm) perl(Test/Warn.pm) perl(parent.pm) perl-devel
# END SourceDeps(oneline)

Epoch: 1
%define m_distro App-Asciio
Name: perl-App-Asciio
Version: 1.9.02
Release: alt1
Summary: Plain ASCII diagram

Group: Graphics
License: Perl
URL: http://search.cpan.org/~nkh/App-Asciio/
VCS: https://github.com/nkh/P5-App-Asciio.git

BuildArch: noarch
Source0: %{name}-%{version}.tar

BuildRequires: xvfb-run perl(Term/Size.pm)
Requires: perl(Term/Size.pm)

%description
This gtk-perl application allows you to draw ASCII diagrams in a modern
(but simple) graphical application. The ASCII graphs can be saved as
ASCII or in a format that allows you to modify them later.

%prep
%setup -q
#patch0 -p1

%build
%def_without test
%perl_vendor_build
xvfb-run -a perl Build test

%install
%perl_vendor_install
rm %buildroot%_bindir/A

# need DISPLAY for perl.req
%{expand:%%global __find_requires xvfb-run -a %__find_requires}

%files
%doc Todo.txt README.md
%_bindir/asciio
%_bindir/asciio_to_text
%perl_vendor_privlib/App/Asciio*

%changelog
* Thu Dec 07 2023 Igor Vlasenko <viy@altlinux.org> 1:1.9.02-alt1
- new version

* Tue Oct 31 2023 Igor Vlasenko <viy@altlinux.org> 1:1.9-alt1
- CPAN update

* Fri Nov 13 2015 Vladimir Lettiev <crux@altlinux.ru> 1.51.3-alt1
- 1.51.3

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02.71-alt2
- fixed test (ignoring warning message)
- fixed check with perl.req

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 1.02.71-alt1
- initial build
