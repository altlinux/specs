%define        pkgname rubocop

Name:          gem-%pkgname
Version:       0.65.0
Release:       alt1
Summary:       A Ruby static code analyzer and formatter.
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubocop.org/
# VCS:         https://github.com/rubocop-hq/rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(bump)
BuildRequires: gem(rack)

%description
A Ruby static code analyzer and formatter, based on the community Ruby style
guide.

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%package       -n %pkgname
Summary:       Executable file for rubocop.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for rubocop.

%description   -n %pkgname -l ru_RU.UTF-8
Исполнямки для рубокопа.

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.65.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
