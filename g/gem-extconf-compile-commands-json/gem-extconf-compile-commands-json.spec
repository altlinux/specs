%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname extconf_compile_commands_json

Name:          gem-extconf-compile-commands-json
Version:       0.0.7
Release:       alt1
Summary:       Generate clangd compile_commands.json files for gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/KJTsanaktsidis/extconf_compile_commands_json
Vcs:           https://github.com/kjtsanaktsidis/extconf_compile_commands_json.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(standard) >= 1.12
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names extconf_compile_commands_json,extconf-compile-commands-json
Requires:      ruby >= 2.6.0
Provides:      gem(extconf_compile_commands_json) = 0.0.7

%description
The extconf_compile_commands_json gem allows you to easily generate compatible
compile_commands.json files from your extconf.rb file. This makes it easy to use
the clangd LSP when working on your gem.


%if_enabled    doc
%package       -n gem-extconf-compile-commands-json-doc
Version:       0.0.7
Release:       alt1
Summary:       Generate clangd compile_commands.json files for gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета extconf_compile_commands_json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(extconf_compile_commands_json) = 0.0.7

%description   -n gem-extconf-compile-commands-json-doc
Generate clangd compile_commands.json files for gems documentation files.

The extconf_compile_commands_json gem allows you to easily generate compatible
compile_commands.json files from your extconf.rb file. This makes it easy to use
the clangd LSP when working on your gem.

%description   -n gem-extconf-compile-commands-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета extconf_compile_commands_json.
%endif


%if_enabled    devel
%package       -n gem-extconf-compile-commands-json-devel
Version:       0.0.7
Release:       alt1
Summary:       Generate clangd compile_commands.json files for gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета extconf_compile_commands_json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(extconf_compile_commands_json) = 0.0.7
Requires:      gem(standard) >= 1.12
Conflicts:     gem(standard) >= 2

%description   -n gem-extconf-compile-commands-json-devel
Generate clangd compile_commands.json files for gems development package.

The extconf_compile_commands_json gem allows you to easily generate compatible
compile_commands.json files from your extconf.rb file. This makes it easy to use
the clangd LSP when working on your gem.

%description   -n gem-extconf-compile-commands-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета extconf_compile_commands_json.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-extconf-compile-commands-json-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-extconf-compile-commands-json-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Sep 05 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.7-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
