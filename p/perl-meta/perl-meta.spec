Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Perform optinal tests
%bcond_without perl_meta_enables_optional_test

Name:           perl-meta
Version:        0.012
Release:        alt1_2
Summary:        Meta-programming API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/meta
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/meta-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests:
BuildRequires:  perl(experimental.pm)
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(Sub/Util.pm)
BuildRequires:  perl(Test2/V0.pm)
%if %{with perl_meta_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
%endif
Source44: import.info

%description
This package provides an API for Perl meta programming; that is, allowing code
to inspect or manipulate parts of its own program structure. Parts of the perl
interpreter itself can be accessed by means of "meta"-objects provided by this
package. Methods on these objects allow inspection of details, as well as
creating new items or removing existing ones.

%package tests
Group: Development/Perl
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n meta-%{version}

%if !%{with perl_meta_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{t/99pod\.t}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Build.PL --installdirs=vendor --optimize='%{optflags}'
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# %{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_meta_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_archlib}/auto/meta
%{perl_vendor_archlib}/meta.pm

%files tests
%{_libexecdir}/%{name}

%changelog
* Wed Apr 09 2025 Igor Vlasenko <viy@altlinux.org> 0.012-alt1_2
- converted for ALT Linux by srpmconvert tools

* Fri Sep 22 2023 Igor Vlasenko <viy@altlinux.org> 0.001-alt1
- initial import by package builder

