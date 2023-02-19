%define        gemname rotp

Name:          gem-rotp
Version:       6.2.2
Release:       alt1
Summary:       A Ruby library for generating and verifying one time passwords
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mdp/rotp
Vcs:           https://github.com/mdp/rotp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(simplecov) >= 0.12
BuildRequires: gem(timecop) >= 0.8
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(timecop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-rotp < %EVR
Provides:      ruby-rotp = %EVR
Provides:      gem(rotp) = 6.2.2


%description
EA ruby library for generating and validating one time passwords (HOTP & TOTP)
according to RFC 4226 and RFC 6238.

ROTP is compatible with Google Authenticator available for Android and iPhone
and any other TOTP based implementations.

Many websites use this for multi-factor authentication, such as GMail, Facebook,
Amazon EC2, WordPress, and Salesforce.


%package       -n rotp
Version:       6.2.2
Release:       alt1
Summary:       A Ruby library for generating and verifying one time passwords executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rotp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rotp) = 6.2.2

%description   -n rotp
A Ruby library for generating and verifying one time passwords
executable(s).

EA ruby library for generating and validating one time passwords (HOTP & TOTP)
according to RFC 4226 and RFC 6238.

ROTP is compatible with Google Authenticator available for Android and iPhone
and any other TOTP based implementations.

Many websites use this for multi-factor authentication, such as GMail, Facebook,
Amazon EC2, WordPress, and Salesforce.

%description   -n rotp -l ru_RU.UTF-8
Исполнямка для самоцвета rotp.


%package       -n gem-rotp-doc
Version:       6.2.2
Release:       alt1
Summary:       A Ruby library for generating and verifying one time passwords documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rotp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rotp) = 6.2.2

%description   -n gem-rotp-doc
A Ruby library for generating and verifying one time passwords documentation
files.

EA ruby library for generating and validating one time passwords (HOTP & TOTP)
according to RFC 4226 and RFC 6238.

ROTP is compatible with Google Authenticator available for Android and iPhone
and any other TOTP based implementations.

Many websites use this for multi-factor authentication, such as GMail, Facebook,
Amazon EC2, WordPress, and Salesforce.

%description   -n gem-rotp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rotp.


%package       -n gem-rotp-devel
Version:       6.2.2
Release:       alt1
Summary:       A Ruby library for generating and verifying one time passwords development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rotp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rotp) = 6.2.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.5
Requires:      gem(simplecov) >= 0.12
Requires:      gem(timecop) >= 0.8
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(timecop) >= 1

%description   -n gem-rotp-devel
A Ruby library for generating and verifying one time passwords development
package.

EA ruby library for generating and validating one time passwords (HOTP & TOTP)
according to RFC 4226 and RFC 6238.

ROTP is compatible with Google Authenticator available for Android and iPhone
and any other TOTP based implementations.

Many websites use this for multi-factor authentication, such as GMail, Facebook,
Amazon EC2, WordPress, and Salesforce.

%description   -n gem-rotp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rotp.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rotp
%doc README.md
%_bindir/rotp

%files         -n gem-rotp-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rotp-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 6.2.2-alt1
- ^ 5.1.0 -> 6.2.2

* Sat Mar 07 2020 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt2
- + lost executable package
- ! spec tags url, vcs

* Fri Jan 31 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- Initial build.
