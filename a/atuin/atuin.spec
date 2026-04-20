%define _unpackaged_files_terminate_build 1

%def_with check

Name: atuin
Version: 18.15.2
Release: alt1

Summary: Magical shell history

License: MIT
Group: Shells
Url: https://github.com/atuinsh/atuin

# Source-url: https://github.com/atuinsh/atuin/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%ifarch loongarch64
# need to rebuild aws-lc-sys
BuildRequires: cmake rust-bindgen clang-devel
%endif

Requires: bash-preexec

%if_with check
BuildRequires: postgresql15
BuildRequires: postgresql15-server
BuildRequires: postgresql15-contrib
%endif

%description
Atuin replaces your existing shell history with a SQLite database, and records
additional context for your commands. Additionally, it provides optional and
fully encrypted synchronization of your history between machines, via an Atuin
server.

%prep
%setup -a1

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF
mkdir completions

%build
%rust_build
for sh in 'bash' 'fish' 'zsh'; do
    "target/release/atuin" gen-completions -s "$sh" -o completions/
done

%install
install -Dm 755 target/release/atuin -t %buildroot%_bindir
install -Dm 644 completions/atuin.bash %buildroot%_datadir/bash-completion/completions/atuin
install -Dm 644 completions/_atuin %buildroot%_datadir/zsh/site-functions/_atuin
install -Dm 644 completions/atuin.fish %buildroot%_datadir/fish/vendor_completions.d/atuin.fish

%check
export PG_BIN="/usr/bin"
export PG_DATA="$TMPDIR/pgdata"
export PG_PORT=54321

rm -rf "${PG_DATA}"
mkdir -p "${PG_DATA}"
chmod 700 "${PG_DATA}"

#Initiate the DB, log outside the data directory
mkdir -p logs

#Important: pipe and line break are combined in one command
"${PG_BIN}/initdb" -D "${PG_DATA}" -U "$(whoami)" --no-locale 2>&1 | tee logs/initdb.log
if [ $? -ne 0 ]; then
    echo "Ошибка initdb."
    cat logs/initdb.log
    exit 1
fi

#Setting up configs
cat <<EOF > "${PG_DATA}/postgresql.conf"
listen_addresses = 'localhost'
port = ${PG_PORT}
unix_socket_directories = '${PG_DATA}'
EOF

echo "host all all 127.0.0.1/32 trust" >> "${PG_DATA}/pg_hba.conf"

#Launch Pg
if ! "${PG_BIN}/pg_ctl" -D "${PG_DATA}" -l logs/start.log start; then
    echo "=== ОШИБКА ЗАПУСКА POSTGRESQL ==="
    [ -f logs/start.log ] && cat logs/start.log || echo "(Лог-файл не создан.)"
    echo "=== Проверка порта ${PG_PORT} ==="
    ss -tulpn | grep ":${PG_PORT}" || true
    ls -lad "${PG_DATA}"
    exit 1
fi

#Waiting for readiness
for i in {1..10}; do
    if "${PG_BIN}/pg_isready" -h localhost -p "${PG_PORT}"; then
        break
    fi
    sleep 2
done

#Create a test database
"${PG_BIN}/createdb" -h localhost -p "${PG_PORT}" atuin

#Exporting environment variable for tests
export ATUIN_DB_URI="postgres:///atuin?host=${PG_DATA}&port=${PG_PORT}"

#Launch tests
%rust_test || ( "${PG_BIN}/pg_ctl" -D "${PG_DATA}" stop && exit 1 )

#Stop Pg
"${PG_BIN}/pg_ctl" -D "${PG_DATA}" stop

%files
%_bindir/atuin
%_datadir/bash-completion/completions/atuin
%_datadir/fish/vendor_completions.d/atuin.fish
%_datadir/zsh/site-functions/_atuin
%doc LICENSE

%changelog
* Mon Apr 20 2026 Ilya Sorochan <k0tran@altlinux.org> 18.15.2-alt1
- new version 18.15.2

* Sat Apr 11 2026 Boris Yumankulov <boria138@altlinux.org> 18.13.6-alt1
- new version 18.13.6

* Wed Feb 18 2026 Boris Yumankulov <boria138@altlinux.org> 18.12.1-alt1
- new version 18.12.1

* Mon Feb 02 2026 Ilya Sorochan <k0tran@altlinux.org> 18.11.0-alt2
- fix FTBFS on loongarch64

* Fri Jan 23 2026 Boris Yumankulov <boria138@altlinux.org> 18.11.0-alt1
- new version 18.11.0

* Sun Oct 26 2025 Boris Yumankulov <boria138@altlinux.org> 18.10.0-alt1
- new version 18.10.0
- add requires to bash-preexec (ALT bug: 56351)

* Tue Sep 09 2025 Boris Yumankulov <boria138@altlinux.org> 18.8.0-alt1
- new version 18.8.0

* Sat May 10 2025 Boris Yumankulov <boria138@altlinux.org> 18.6.1-alt1
- new version 18.6.1

* Mon Apr 21 2025 Boris Yumankulov <boria138@altlinux.org> 18.5.0-alt1
- new version 18.5.0
- enable check thanks @xeno for code

* Sat Apr 12 2025 Boris Yumankulov <boria138@altlinux.org> 18.4.0-alt1
- initial build for ALT Sisyphus

