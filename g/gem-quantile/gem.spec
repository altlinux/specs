%define        pkgname quantile

Name:          gem-%pkgname
Version:       0.2.1
Release:       alt1
Summary:       Graham Cormode and S. Muthukrishnan's Effective Computation of Biased Quantiles over Data Streams in ICDE'05
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/matttproud/ruby_quantile_estimation
%vcs           https://github.com/matttproud/ruby_quantile_estimation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Ruby Implementation of Graham Cormode and S. Muthukrishnan's Effective
Computation of Biased Quantiles over Data Streams in ICDE'05.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


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

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
