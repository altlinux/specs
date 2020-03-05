%define        pkgname rotp

Name:          gem-%pkgname
Version:       5.1.0
Release:       alt2
Summary:       A Ruby library for generating and verifying one time passwords
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/mdp/rotp
Vcs:           https://github.com/mdp/rotp.git

Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
BuildRequires: gem(simplecov)
BuildRequires: gem(timecop)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
EA ruby library for generating and validating one time passwords (HOTP & TOTP)
according to RFC 4226 and RFC 6238.

ROTP is compatible with Google Authenticator available for Android and iPhone
and any other TOTP based implementations.

Many websites use this for multi-factor authentication, such as GMail, Facebook,
Amazon EC2, WordPress, and Salesforce.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemsdocdir/*

%files         -n %pkgname
%_bindir/%pkgname


%changelog
* Sat Mar 07 2020 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt2
- + lost executable package
- ! spec tags url, vcs

* Fri Jan 31 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- Initial build.
