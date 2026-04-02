%global import_path github.com/TwiN/gatus/v5

Name: gatus
Version: 5.35.0
Release: alt1

Summary: Automated developer-oriented status page
License: Apache-2.0
Group: Monitoring
Url: https://gatus.io
Vcs: https://github.com/TwiN/gatus

Source0: %name-%version.tar
Source1: vendor.tar
Source2: gatus.service
Source3: config.yaml

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.5

%description
Gatus is a developer-oriented health dashboard that gives you the ability to
monitor your services using HTTP, ICMP, TCP, and even DNS queries as well as
evaluate the result of said queries by using a list of conditions on values
like the status code, the response time, the certificate expiration, the body
and many others. The icing on top is that each of these health checks can be
paired with alerting via Slack, Teams, PagerDuty, Discord, Twilio and many
more.

%prep
%setup -a 1

sed -i 's|DefaultConfigurationFilePath = .*|DefaultConfigurationFilePath = "/etc/%name/config.yaml"|' config/config.go
sed -i 's|DefaultFallbackConfigurationFilePath = .*|DefaultFallbackConfigurationFilePath = "/etc/%name/config.yml"|' config/config.go

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -pD -m0644 %SOURCE2 %buildroot%_unitdir/gatus.service
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/%name/config.yaml

mkdir -p %buildroot%_localstatedir/%name

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -M -d %_localstatedir/%name -s /dev/null \
    -c "Gatus user" _%name > /dev/null 2>&1 ||:

%post
%post_systemd gatus.service

%preun
%preun_systemd gatus.service

%files
%doc *.md
%_bindir/gatus
%config(noreplace) %_sysconfdir/%name/config.yaml
%_unitdir/gatus.service
%attr(775, _%name, _%name) %dir %_localstatedir/%name

%changelog
* Thu Apr 02 2026 Alexander Stepchenko <geochip@altlinux.org> 5.35.0-alt1
- 5.30.0 -> 5.35.0.

* Wed Nov 05 2025 Alexander Stepchenko <geochip@altlinux.org> 5.30.0-alt1
- 5.29.0 -> 5.30.0.

* Tue Oct 28 2025 Alexander Stepchenko <geochip@altlinux.org> 5.29.0-alt1
- Initial build.
