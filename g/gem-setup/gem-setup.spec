%define        __setup_rb GEM_HOME=%ruby_gemhome %__ruby -I "\$(pwd)/lib" $(which setup-rb 2>/dev/null || which setup)
%define        pkgname setup

Name:          gem-%pkgname
Version:       5.999.6
Release:       alt12
Summary:       Ruby's Classic Site Installer
Group:         Development/Ruby
License:       BSD-2-Clause
Url:           https://github.com/rubyworks/setup
Vcs:           https://github.com/majioa/setup.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Autoreq:       no
Autoprov:      no

Source:        %name-%version.tar
Patch:         patch.patch

BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %_libexecdir/**/*
%add_findprov_skiplist %_libexecdir/**/*
Requires:      chrpath
Requires:      setup-rb
Provides:      gem(setup) = %version

%description
Every well practiced Rubyist is aware of Minero Aoki's ever setup.rb script.
It's how most of us used to install our Ruby programs before RubyGems came
along. And it's still mighty useful in certain scenarios, not the least of
which is the job of the distro package maintainer.

Ruby Setup converts setup.rb into a stand-alone application. No longer
requiring the distribution of the setup.rb script with every Ruby package.
Just instruct one's users to install Ruby Setup (gem install setup) and go from
there. As long as a project is setup.rb compliant, as most are, then there is
little to nothing it's developer must do.


%package       -n setup-rb
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch
Requires:      gem(setup) = %version

%description   -n setup-rb
Executable file for %gemname gem.

%description   -n setup-rb -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Requires:      gem(setup) = %version

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup
%patch -p1

%build
export PATH=$PATH:$(pwd)/bin
%__setup_rb build --use=setup --version-replace=%version

%install
export PATH=$PATH:$(pwd)/bin
%__setup_rb install --install_prefix=%buildroot

%check
export PATH=$PATH:$(pwd)/bin
%__setup_rb test

%files
%doc README* HISTORY*
%ruby_gemspec
%ruby_gemlibdir

%files         -n setup-rb
%doc README*
%ruby_bindir/setup-rb

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt12
- ! some updates

* Thu Jun 06 2024 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt11
- + added support for predeps generator

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt10
- + added support for gem plugins
- ! fixed %%__setup_rb macro

* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt9
- * BREAK: setup exec moved into %%ruby_bindir
- * renamed setup.rb to setup-rb
- ! parse makefile if no target folder defined
- ! touch gem.build_completre anyway even real compilation isn't performed

* Thu Oct 19 2023 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt8
- ! fixed jeweler spec detecton by using class variable storage

* Fri Jan 20 2023 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt7
- * crop upper bound for requires
- ! alias detection for sources with current source name autoaliased
- ! version detection for Hoe module
- ! use self spec array for a gem DSL, or DSL's gemspec array for Gemfile
- - using ruby-gem and rubygem dep prefixes
- ! bones gemspec parser
- ! ruby version deps renderer

* Tue Dec 20 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt6
- + some new options to mkmf when compilation is enabled

* Thu Nov 24 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt5
- ! ridir to docdir with ri arg, to support old rubies

* Sun Sep 30 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt4
- ! fix hoe loading with version detection

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt3
- ! fix to gem build file placement

* Sat Jun 18 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt2
- * merge the same named specs

* Sun May 01 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.6-alt1
- + novel yamlto support when YAML parsings
- + log-level, debug-io, info-io CLI args
- + loaders for ruby, manifest, cmake, git-version-gen, mast, pom XML, rookbook,
    yaml
- + log module to support advanced IO flow logging
- + hoe parser
- !fix loading concerns
- !fix some parsers
- !fix setup default gem generator extension require when real gem is erroneous
- !fix minor loader, and rakefile gemspec bugs
- *changed rake app based on loader
- *changed deps dsl detection
- *changed slightly sources
- -remove gemspec-based parser

* Thu Mar 03 2022 Pavel Skrylev <majioa@altlinux.org> 5.999.5-alt12
- ! for jeweler, and some others spec parser to properly load and store specs

* Mon Oct 25 2021 Pavel Skrylev <majioa@altlinux.org> 5.999.5-alt11
- ^ 5.999.4 -> 5.999.5
- ! pass option hash to gem requirement constructor in setup deps

* Tue Oct 12 2021 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt11
- * extconf module to class, to allow multiext config support.
- + rakefile gemspec finder... but it seems useless though

* Fri Sep 10 2021 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt10
- + gem changing version on-the-fly
- * running extconf as loading the script not forking new ruby instance
- * the headers taken into consideration are only predefined
- * reassignation some souces sequence
- * allow loading gemspec as YAML doc
- * trapping calls to git executable

* Sun Apr 25 2021 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt9
- ! replaces req prefix ruby-gem with gem
- ! other things

* Tue Dec 29 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt8
- ! ls-files of git to list proper files
- * renamed compile to make action
- ! pre key now to affect only make action

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt7
- ! proper detection for requires / provides
- * sort the uniq requires for combined targets

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt6
- ! workaround to remove the "!ruby/array:Files" from yaml

* Sun Nov 22 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt5
- ! trash in provides for packages with prebuild task enabled

* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt4
- + using gut ls-files when no git app

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt3
- ! gemfile dep export in one line when dep name is the same
- ! spec syntax

* Thu Jul 09 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt2
- - additional config path part for config folder for gem target

* Tue Jun 30 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.4-alt1
- ^ 5.999.3 -> 5.999.4
- + actor module
- + 3 actors: copy, link, touch
- + dep-source command line key, to define a name of a source for the
    specified used source, and set to show requires
- + append and skip lists support in source gem and gemfile
- + check to wheither the gemfile is exist, if no skip install
- + echoe spec core extension module
- + echo gemspec parser
- + gemspec detector for bones gemspec types
- + bones extension for core
- + blank method to replace embedded one in gem's specification class
- + autorequire for olddoc and wrongdoc modules if no
- + simple replacement for gem olddoc
- + simple replacement for gem wrongdoc
- + check to wheither the gemfile is exist, if no skip install
- + log module
- - unnecessary deps
- - duplication extfiles due to block in gem source module
- * installation of compiled modules by actors
- * gemspec scheme enumeration and requiring
- * name of rakefile to package task gemspec load
- * gemspecs evaluating and loading in module space for bones, echoe, hoe
    and package task
- * proper loading Rakefile into named module instead of unnamed to
    allowing root level defined methods access
- ! rookbook gemspec detector

* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt15
- - explicit use of prefixes key in build section

* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt14
- + default prefixes to 'gem' value

* Wed Apr 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt13
- + separation prefixes and suffixes when detection the context (lib/bin/...)
- ! lost prefixes key into build macro (fixes #38337)

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt12
- - erroneous glob lib ext method

* Thu Mar 19 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt11
- * libdir replaced to libexecdir for ruby site target

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt10
- ! call to setup.rb with default pure %%__setup_rb

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt9
- ! spec according changlelog policy
- + making lost executables again workable (closes #37180)

* Mon Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt8
- - mistake in dependecies detection for Gemfile source
- ! default datadir to libdir for site ruby packages
- ! getting task list from MultiTask instead of Task
- + load rake task imports before executio pre tasks
- ! state dir for gem target from localstatedir to datadir
- + logdir option, and its processing
- ! installer's group methods
- ! options parser for sources to make both key and value changeable
- ! options pass via parser for rakefile source
- ! object class options store to specfic one by changing from @@ to @.
- + ronn man detection and compilation
- + prefixes command line parameter: gem,ruby...
- + source directory groups command line parameters: --src<param>dirs
- ! source module parameter parsing
- + String#pluralize
- + spec selection from Gem::PackageTask object for Rakefile
- - Require dirs detection mistake, not filters out only path with the beginning
  '/'
- - Hoe presence detection error
- + Rookbook gemspec parser (example: erubis gem)
- - Olddoc syntax typo
- - Hoe syntax typo
- + try load hoe gem in the beginning of the how gemspec module
- + support for group trees instead of file lists in sources
- - installation module to support trees
- - compilation modules supporting trees
- - dep module supporting trees
- - bin group name to exe in sources and targets
- - include group name to inc in sources and targets
- - etc group name to conf in sources and targets
- - lost methods in ruby target
- + some kernel methods
- - Prefix remove alias "rails-plugin" for packages
- - Gemfile installation for the Gemfile source is used for gem version
  replacements
- - ERROR msg profix replaced with WARN
- - fix DSL dependenciy replace list for #to_gemfile
- - added compatibility call to external program to do some things for the
  action with --compat=/path/to/program
- - fixed name of the gem file to Gemfile
- - fix loading and saving version replace list for the common and source parts
- - added gem replace verison list argument to gemfile source

* Tue Apr 30 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt7
- Set default external CP to UTF8

* Tue Apr 23 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt6
- - added default value for __dir__ variable, when loading Rakefile info a module,
  this fixes unknown error when adding the var info "$:"
- - separated Hoe gemspec detector from the Rakefile one leading to
  correct evaluation of Rakefile in main space
- - Now old shebang args in the ruby executables will be passed to new
  shebang line
- - Fix sequence so Rakefile will be proceeded before Olddoc gemspecs.
- - Rakefile gemspec detector not will not fall when rakefile name is
  nil
- ! Redone gemspec procedure detection so sequence of gemspecs will be
  affected rather than filelist as before
- Parse olddoc gemspecs before rakefile ones
- Disable adaptive configuration on .so compilation, so extconf.rb will
  be run anytime
- + save aliases also for project and sources
- + add #has_name? to Source::Base to match alises also
- + hot on-source-load gem source version replacement
- + command line for source version replacement called as
  --version-replace
- + added call to chrpath binary to remove RPATH from .so during
  compile action
- - Merged detection of the gemfile in hoe or plain rakefile
- - Removed hoe/debug module
- + inferring gemfile from Rakefile, so when spec is defined in the
  Rakefile it will be detected
- - Fix class name for target ruby from erroneous Site to Ruby
- - Fix install folder for i586 arch, so .so files will be installed by
  using x86 arch

* Sat Apr 06 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt5
- fix req deps on executables when they are already installed only
- set autoalias on binaries only for its source not others, and when no
  other source names match the binary

* Tue Apr 02 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt4
- load Gemfile by temporary changing the root when creating the bundler's DSL

* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt3
- fix requires deps detection over executable's shebang line

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt2
- Added novel approach to detect the dependencies of packages

* Sun Mar 17 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.3-alt1
- Bump to 5.999.3

* Thu Mar 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.2-alt1
- Bump to 5.999.2
- Use Ruby Policy 2.0

* Mon Mar 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.1-alt1
- Bump to 5.999.1

* Fri Jan 25 2019 Pavel Skrylev <majioa@altlinux.org> 5.999.0-alt1
- Initial gemified build for Sisyphus with usage Ruby Policy 2.0.
