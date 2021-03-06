# RPM Spec for git-crypt 
git-crypt spec file created for **Fedora** and **CentOS** following the Fedora [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelinesa).

**Tested on:**  
- Fedora 20
- Fedora 21
- CentOS 7

## Let's build an RPM
> export spec="~/rpmbuild/SPECS"  
> sudo yum install fedora-packager rpmdevtools  
> rpmdev-setuptree  
> git clone https://github.com/Charg/git-crypt-rpm ${spec}  
> spectool -g -R ${spec}/git-crypt.spec  
> sudo yum-builddep ${spec}/git-crypt.spec  
> rpmbuild -ba ${spec}/git-crypt.spec  

You should now see your git-crypt RPM sitting in `~/rpmbuild/RPMS/x86_64`.
