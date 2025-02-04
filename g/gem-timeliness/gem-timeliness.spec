%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname timeliness

Name:          gem-timeliness
Version:       0.5.1
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
%if_enabled check
BuildRequires: gem(activesupport) >= 3.2
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(i18n) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(tzinfo) >= 0.3.31
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Provides:      gem(timeliness) = 0.5.1

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


%if_enabled    doc
%package       -n gem-timeliness-doc
Version:       0.5.1
Release:       alt1
Summary:       Fast date/time parsing for the control freak documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timeliness
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timeliness) = 0.5.1

%description   -n gem-timeliness-doc
Fast date/time parsing for the control freak documentation files.

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
%endif


%if_enabled    devel
%package       -n gem-timeliness-devel
Version:       0.5.1
Release:       alt1
Summary:       Fast date/time parsing for the control freak development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timeliness
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timeliness) = 0.5.1
Requires:      gem(activesupport) >= 3.2
Requires:      gem(appraisal) >= 0
Requires:      gem(base64) >= 0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(i18n) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(mutex_m) >= 0
Requires:      gem(rspec) >= 3.4
Requires:      gem(timecop) >= 0
Requires:      gem(tzinfo) >= 0.3.31
Conflicts:     gem(rspec) >= 4

%description   -n gem-timeliness-devel
Fast date/time parsing for the control freak development package.

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
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.rdoc LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-timeliness-doc
%doc CHANGELOG.rdoc LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-timeliness-devel
%doc CHANGELOG.rdoc LICENSE README.rdoc
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- ^ 0.4.4 -> 0.5.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt1
- ^ 0.4.3 -> 0.4.4

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- + packaged gem with usage Ruby Policy 2.0
