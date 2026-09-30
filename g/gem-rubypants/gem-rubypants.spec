%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubypants

Name:          gem-rubypants
Version:       0.7.0
Release:       alt1
Summary:       RubyPants is a Ruby port of the smart-quotes library SmartyPants
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jmcnevin/rubypants
Vcs:           https://github.com/jmcnevin/rubypants.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Provides:      gem(rubypants) = 0.7.0

%description
The original "SmartyPants" is a free web publishing plug-in for Movable Type,
Blosxom, and BBEdit that easily translates plain ASCII punctuation characters
into "smart" typographic punctuation HTML entities.


%if_enabled    doc
%package       -n gem-rubypants-doc
Version:       0.7.0
Release:       alt1
Summary:       RubyPants is a Ruby port of the smart-quotes library SmartyPants documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubypants
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubypants) = 0.7.0

%description   -n gem-rubypants-doc
RubyPants is a Ruby port of the smart-quotes library SmartyPants documentation
files.

The original "SmartyPants" is a free web publishing plug-in for Movable Type,
Blosxom, and BBEdit that easily translates plain ASCII punctuation characters
into "smart" typographic punctuation HTML entities.

%description   -n gem-rubypants-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubypants.
%endif


%if_enabled    devel
%package       -n gem-rubypants-devel
Version:       0.7.0
Release:       alt1
Summary:       RubyPants is a Ruby port of the smart-quotes library SmartyPants development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubypants
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubypants) = 0.7.0
Requires:      gem(codecov) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-rubypants-devel
RubyPants is a Ruby port of the smart-quotes library SmartyPants development
package.

The original "SmartyPants" is a free web publishing plug-in for Movable Type,
Blosxom, and BBEdit that easily translates plain ASCII punctuation characters
into "smart" typographic punctuation HTML entities.

%description   -n gem-rubypants-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubypants.
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
%doc LICENSE.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubypants-doc
%doc LICENSE.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubypants-devel
%doc LICENSE.rdoc README.rdoc
%endif


%changelog
* Mon Jun 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
