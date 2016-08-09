# Note:
# You will need to move generated scripts in the namespace/class closing braces
#
# Command:
# python generator.py all MyModule/MyResource
# -or- one each resource
# python generator.py list MyModule/MyResource
# python generator.py post MyModule/MyResource
# python generator.py get MyModule/MyResource
# python generator.py put MyModule/MyResource
# python generator.py delete MyModule/MyResource

import os
import sys


### IMPlEMENTATION
verb = sys.argv[1].lower()
module, resource = sys.argv[2].split("/")

if not verb:
    verb = "all"

if not module:
    module = "<<ModuleName>>"

if not resource:
    resource = "<<ResourceName>>"

# Request
filename = "Implementation/Drachpy.<<ModuleName>>.API/Request/Request.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "list")):
        writer.write("""
    public class Get<<ResourceName>>ListRequestValidator : AbstractValidator<Get<<ResourceName>>ListRequest>
    {
        public Get<<ResourceName>>ListRequestValidator()
        {
        }
    }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
    public class Post<<ResourceName>>RequestValidator : AbstractValidator<Post<<ResourceName>>Request>
    {
        public Post<<ResourceName>>RequestValidator()
        {
            RuleFor(r => r.Id).NotNull();
        }
    }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
    public class Get<<ResourceName>>RequestValidator : AbstractValidator<Get<<ResourceName>>Request>
    {
        public Get<<ResourceName>>RequestValidator()
        {
            RuleFor(r => r.Id).NotNull();
        }
    }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
    public class Put<<ResourceName>>RequestValidator : AbstractValidator<Put<<ResourceName>>Request>
    {
        public Put<<ResourceName>>RequestValidator()
        {
            RuleFor(r => r.Id).NotNull();
        }
    }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
    public class Delete<<ResourceName>>RequestValidator : AbstractValidator<Delete<<ResourceName>>Request>
    {
        public Delete<<ResourceName>>RequestValidator()
        {
            RuleFor(r => r.Id).NotNull();
        }
    }
        """.replace("<<ResourceName>>", resource))
# Route
filename = "Implementation/Drachpy.<<ModuleName>>.API/Request/Route.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "list")):
        writer.write("""
            appHost.Routes.Add<Get<<ResourceName>>ListRequest>("/service/api/<<ModuleName>>/<<ResourceName>>", "GET");
        """.replace("<<ModuleName>>", module).replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
            appHost.Routes.Add<Post<<ResourceName>>Request>("/service/api/<<ModuleName>>/<<ResourceName>>", "POST");
        """.replace("<<ModuleName>>", module).replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
            appHost.Routes.Add<Get<<ResourceName>>Request>("/service/api/<<ModuleName>>/<<ResourceName>>/{id}", "GET");
        """.replace("<<ModuleName>>", module).replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
            appHost.Routes.Add<Put<<ResourceName>>Request>("/service/api/<<ModuleName>>/<<ResourceName>>/{id}", "PUT");
        """.replace("<<ModuleName>>", module).replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
            appHost.Routes.Add<Delete<<ResourceName>>Request>("/service/api/<<ModuleName>>/<<ResourceName>>/{id}", "DELETE");
        """.replace("<<ModuleName>>", module).replace("<<ResourceName>>", resource))

# ApiService
filename = "Implementation/Drachpy.<<ModuleName>>.API/Service/<<ModuleName>>ApiService.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "list")):
        writer.write("""
        public Get<<ResourceName>>ListResponse Get(Get<<ResourceName>>ListRequest request)
        {
            return service.Get<<ResourceName>>List(request);
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
        public Post<<ResourceName>>Response Post(Post<<ResourceName>>Request request)
        {
            return service.Post<<ResourceName>>(request);
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
        public Get<<ResourceName>>Response Get(Get<<ResourceName>>Request request)
        {
            return service.Get<<ResourceName>>(request);
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
        public Put<<ResourceName>>Response Put(Put<<ResourceName>>Request request)
        {
            return service.Put<<ResourceName>>(request);
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
        public Delete<<ResourceName>>Response Delete(Delete<<ResourceName>>Request request)
        {
            return service.Delete<<ResourceName>>(request);
        }
        """.replace("<<ResourceName>>", resource))

# Service
filename = "Implementation/Drachpy.<<ModuleName>>.BusinessLogic/Service/<<ModuleName>>Service.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "list")):
        writer.write("""
        public Get<<ResourceName>>ListResponse Get<<ResourceName>>List(Get<<ResourceName>>ListRequest request)
        {
            throw new NotImplementedException();
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
        public Post<<ResourceName>>Response Post<<ResourceName>>(Post<<ResourceName>>Request request)
        {
            throw new NotImplementedException();
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
        public Get<<ResourceName>>Response Get<<ResourceName>>(Get<<ResourceName>>Request request)
        {
            throw new NotImplementedException();
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
        public Put<<ResourceName>>Response Put<<ResourceName>>(Put<<ResourceName>>Request request)
        {
            throw new NotImplementedException();
        }
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
        public Delete<<ResourceName>>Response Delete<<ResourceName>>(Delete<<ResourceName>>Request request)
        {
            throw new NotImplementedException();
        }
        """.replace("<<ResourceName>>", resource))


### INTERFACE
# Model
filename = "Interface/Drachpy.<<ModuleName>>.BusinessLogic.Interface/Model/<<ModuleName>>Model.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "delete")):
        writer.write("""
    #region Get<<ResourceName>>List
    public class Get<<ResourceName>>ListResponse { }
    public class Get<<ResourceName>>ListRequest { }
    #endregion Get<<ResourceName>>List
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
    #region Post<<ResourceName>>
    public class Post<<ResourceName>>Response { }
    public class Post<<ResourceName>>Request
    {
        public int Id { get; set; }
    }
    #endregion Post<<ResourceName>>
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
    #region Get<<ResourceName>>
    public class Get<<ResourceName>>Response { }
    public class Get<<ResourceName>>Request
    {
        public int Id { get; set; }
    }
    #endregion Get<<ResourceName>>
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
    #region Put<<ResourceName>>
    public class Put<<ResourceName>>Response { }
    public class Put<<ResourceName>>Request
    {
        public int Id { get; set; }
    }
    #endregion Put<<ResourceName>>
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
    #region Delete<<ResourceName>>
    public class Delete<<ResourceName>>Response { }
    public class Delete<<ResourceName>>Request
    {
        public int Id { get; set; }
    }
    #endregion Delete<<ResourceName>>
        """.replace("<<ResourceName>>", resource))

# ServiceInterface
filename = "Interface/Drachpy.<<ModuleName>>.BusinessLogic.Interface/Service/I<<ModuleName>>Service.cs".replace("<<ModuleName>>", module)
dir = os.path.dirname(filename)
if not os.path.exists(dir):
    os.makedirs(dir)

with open(filename, "a") as writer:
    if (verb in ("all", "delete")):
        writer.write("""
        Get<<ResourceName>>ListResponse Get<<ResourceName>>(Get<<ResourceName>>ListRequest request);
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "post")):
        writer.write("""
        Post<<ResourceName>>Response Post<<ResourceName>>(Post<<ResourceName>>Request request);
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "get")):
        writer.write("""
        Get<<ResourceName>>Response Get<<ResourceName>>(Get<<ResourceName>>Request request);
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "put")):
        writer.write("""
        Put<<ResourceName>>Response Put<<ResourceName>>(Put<<ResourceName>>Request request);
        """.replace("<<ResourceName>>", resource))

    if (verb in ("all", "delete")):
        writer.write("""
        Delete<<ResourceName>>Response Delete<<ResourceName>>(Delete<<ResourceName>>Request request);
        """.replace("<<ResourceName>>", resource))
