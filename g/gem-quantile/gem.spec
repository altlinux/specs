%define        gemname quantile

Name:          gem-quantile
Version:       0.2.1
Release:       alt1.1
Summary:       Graham Cormode and S. Muthukrishnan's Effective Computation of Biased Quantiles over Data Streams in ICDE'05
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/matttproud/ruby_quantile_estimation
Vcs:           https://github.com/matttproud/ruby_quantile_estimation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(quantile) = 0.2.1


%description
Ruby Implementation of Graham Cormode and S. Muthukrishnan's Effective
Computation of Biased Quantiles over Data Streams in ICDE'05.


%package       -n gem-quantile-doc
Version:       0.2.1
Release:       alt1.1
Summary:       Graham Cormode and S. Muthukrishnan's Effective Computation of Biased Quantiles over Data Streams in ICDE'05 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета quantile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(quantile) = 0.2.1

%description   -n gem-quantile-doc
Graham Cormode and S. Muthukrishnan's Effective Computation of Biased Quantiles
over Data Streams in ICDE'05 documentation files.

Ruby Implementation of Graham Cormode and S. Muthukrishnan's Effective
Computation of Biased Quantiles over Data Streams in ICDE'05.

%description   -n gem-quantile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета quantile.


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

%files         -n gem-quantile-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1.1
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
