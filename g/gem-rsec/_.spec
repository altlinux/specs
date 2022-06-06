%define        gemname rsec

Name:          gem-rsec
Version:       1.0.0
Release:       alt1.1
Summary:       Parser / Regexp Combinator For Ruby
License:       Ruby
Group:         Development/Ruby
Url:           http://rsec.herokuapp.com
Vcs:           https://github.com/luikore/rsec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rsec) = 1.0.0


%description
Easy and extreme fast dynamic PEG parser combinator.

PEG grammar for Ruby, based on StringScanner. Consistently superior speed: up to
10 times faster than Treetop, and twice the speed of rex+racc.

Compatible with Ruby v1.9 and above.


%package       -n gem-rsec-doc
Version:       1.0.0
Release:       alt1.1
Summary:       Parser / Regexp Combinator For Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rsec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rsec) = 1.0.0

%description   -n gem-rsec-doc
Parser / Regexp Combinator For Ruby documentation files.

Easy and extreme fast dynamic PEG parser combinator.

PEG grammar for Ruby, based on StringScanner. Consistently superior speed: up to
10 times faster than Treetop, and twice the speed of rex+racc.

Compatible with Ruby v1.9 and above.

%description   -n gem-rsec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rsec.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rsec-doc
%doc readme.rdoc
%ruby_gemdocdir


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ! spec

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
