%define        gemname timeliness

Name:          gem-timeliness
Version:       0.4.4
Release:       alt1
Summary:       Fast date/time parsing for the control freak
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/adzap/timeliness
Vcs:           https://github.com/adzap/timeliness.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 3.2 gem(activesupport) < 7
BuildRequires: gem(tzinfo) >= 0.3.31
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(i18n) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
Provides:      gem(timeliness) = 0.4.4


%description
Date/time parser for Ruby with the following features:

* Extensible with custom formats and tokens.
* It's pretty fast. Up to 60% faster than Time/Date parse method.
* Control the parser strictness.
* Control behaviour of ambiguous date formats (US vs European e.g. mm/dd/yy,
  dd/mm/yy).
* I18n support (for months), if I18n gem loaded.
* Fewer WTFs than Time/Date parse method.
* Has no dependencies.
* Works with Ruby MRI >= 2.2

Extracted from the validates_timeliness gem, it has been rewritten cleaner and
much faster. It's most suitable for when you need to control the parsing
behaviour. It's faster than the Time/Date class parse methods, so it has general
appeal.


%package       -n gem-timeliness-doc
Version:       0.4.4
Release:       alt1
Summary:       Fast date/time parsing for the control freak documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timeliness
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timeliness) = 0.4.4

%description   -n gem-timeliness-doc
Fast date/time parsing for the control freak documentation
files.

Date/time parser for Ruby with the following features:

* Extensible with custom formats and tokens.
* It's pretty fast. Up to 60% faster than Time/Date parse method.
* Control the parser strictness.
* Control behaviour of ambiguous date formats (US vs European e.g. mm/dd/yy,
dd/mm/yy).
* I18n support (for months), if I18n gem loaded.
* Fewer WTFs than Time/Date parse method.
* Has no dependencies.
* Works with Ruby MRI >= 2.2

Extracted from the validates_timeliness gem, it has been rewritten cleaner and
much faster. It's most suitable for when you need to control the parsing
behaviour. It's faster than the Time/Date class parse methods, so it has general
appeal.

%description   -n gem-timeliness-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timeliness.


%package       -n gem-timeliness-devel
Version:       0.4.4
Release:       alt1
Summary:       Fast date/time parsing for the control freak development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timeliness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timeliness) = 0.4.4
Requires:      gem(activesupport) >= 3.2 gem(activesupport) < 7
Requires:      gem(tzinfo) >= 0.3.31
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(timecop) >= 0
Requires:      gem(i18n) >= 0

%description   -n gem-timeliness-devel
Fast date/time parsing for the control freak development
package.

Date/time parser for Ruby with the following features:

* Extensible with custom formats and tokens.
* It's pretty fast. Up to 60% faster than Time/Date parse method.
* Control the parser strictness.
* Control behaviour of ambiguous date formats (US vs European e.g. mm/dd/yy,
dd/mm/yy).
* I18n support (for months), if I18n gem loaded.
* Fewer WTFs than Time/Date parse method.
* Has no dependencies.
* Works with Ruby MRI >= 2.2

Extracted from the validates_timeliness gem, it has been rewritten cleaner and
much faster. It's most suitable for when you need to control the parsing
behaviour. It's faster than the Time/Date class parse methods, so it has general
appeal.

%description   -n gem-timeliness-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета timeliness.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-timeliness-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-timeliness-devel
%doc README.rdoc


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt1
- ^ 0.4.3 -> 0.4.4

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- + packaged gem with usage Ruby Policy 2.0
