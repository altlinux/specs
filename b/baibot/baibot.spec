%define _unpackaged_files_terminate_build 1
%def_disable check

%define user_name _baibot
%define group_name _baibot

Name:    baibot
Version: 1.24.0
Release: alt1
Summary: Matrix bot for AI LLM capabilities (text-generation, TTS, STT, image-generation)
License: AGPL-3.0-or-later
Group:   Networking/Instant messaging
URL:     https://github.com/etkecc/baibot
VCS:     https://github.com/etkecc/baibot.git

ExcludeArch: %arm %ix86
Source:  %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Source3: %name.service
Source4: sysusers
Patch1:  %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libsqlite3-devel
BuildRequires: gcc-c++

%description
baibot is a Matrix bot built by etke.cc for using different capabilities of
AI / Large Language Models: text-generation, speech-to-text, text-to-speech and
image-generation, across many providers (Anthropic, OpenAI, Groq, LocalAI,
Ollama and others). It runs everything in-process, supports encrypted Matrix
rooms and runtime configuration via chat commands.

%prep
%setup -a1
%patch1 -p1
%rust_prep
cat %SOURCE2 >> .cargo/config.toml

%build
%rust_build
%if_enabled check
%rust_test --no-run --workspace --offline
%endif

%install
%rust_install
install -Dm644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm644 %SOURCE4 %buildroot%_sysusersdir/%name.conf
sed -i -e 's/__USER__/%user_name/g' -e 's/__GROUP__/%group_name/g' \
    %buildroot%_unitdir/%name.service %buildroot%_sysusersdir/%name.conf
install -Dm644 etc/app/config.yml.dist %buildroot%_sysconfdir/%name/config.yml
mkdir -p %buildroot%_localstatedir/%name

%check
%rust_test --workspace --offline

%pre
groupadd -r -f %group_name
useradd -r -M -g %group_name -c 'baibot Matrix AI bot' -d %_localstatedir/%name -s /sbin/nologin %user_name >/dev/null 2>&1 ||:

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc LICENSE README.md
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %attr(640,root,%group_name) %_sysconfdir/%name/config.yml
%dir %attr(750,%user_name,%group_name) %_localstatedir/%name

%changelog
* Fri Jun 26 2026 Alexey Shabalin <shaba@altlinux.org> 1.24.0-alt1
- updated from 1.21.1 to 1.24.0

* Thu Jun 18 2026 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt3
- Enable ureq "native-certs" feature so the openai-compatible provider
  trusts the system CA store instead of only the bundled webpki-roots
  (fixes UnknownIssuer against endpoints behind a private/internal CA).
- Revert "Build async-openai with native-tls".

* Thu Jun 18 2026 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt2
- Build async-openai with native-tls (use the system CA trust store).

* Tue Jun 16 2026 Alexey Shabalin <shaba@altlinux.org> 1.21.1-alt1
- Initial build.
