%define        pkgname powerbar

Name:          gem-%pkgname
Version:       2.0.1
Release:       alt1
Summary:       The last progressbar-library you'll ever need
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/busyloop/powerbar
%vcs           https://github.com/busyloop/powerbar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
This is PowerBar - The last progressbar-library you'll ever need.

- Detects when stdout is not a terminal and automatically falls back to logging

 * Does not clutter your log-files with ansi-codes!
 * If your CLI-app can run interactively and non-interactively (e.g. cronjob)
   you will automatically get reasonable progress-output in both modes.
 * By default prints to stderr but can call any output-method of your choice
   (e.g. your favorite Logger).

- Fully customizable; all output is template-driven.

- All output is optional. You may set PowerBar to silently collect progress
  information (percentage-done, throughput, ETA, etc.) and then use
  the computed values elsewhere in your app.

- All state can be updated at any time. For example: If you're monitoring
  a multi-part operation then you can change the status-message of a running
  PowerBar to reflect the current state.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%_bindir/%{pkgname}*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
