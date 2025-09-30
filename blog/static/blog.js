   //new post /post
    const add = document.querySelector(".add")
    const newpost = document.querySelector(".newpost")

    if (add && newpost) {
    add.addEventListener('click', ()=>{
        newpost.innerHTML = `<div class="card text-center z-3 fixed-top mx-auto m-3 bg-secondary p-3"style="top: 3em; width: 80%; ">
        <div class="d-flex align-items-center justify-content-between p-1  m-0"> 
        <img class="rounded-circle border border-1 m-2" src="{{ i.info[1] }}" alt="" style="width: 3em;">
        <p><button class="X ">X</button></p>
        </div>
        <form action="/post" method="post">
        <div class="input-group mb-3">
          <input type="text" name="title" class="form-control" placeholder="Title" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group input-group-sm mb-3" style ="height: 5em">
          <input type="text" name="desc" class="form-control" placeholder="Description" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">
        </div>

          <div class="input-group mb-3 " >
          <label class="input-group-text" for="inputGroupSelect01">Topic</label>
          <select class="form-select" name="topic" id="inputGroupSelect01">
            <option selected>Choose...</option>
            <option value="Travel">Travel</option>
            <option value="Fashion">Fashion</option>
            <option value="Tech">Tech</option>
            <option value="Education">Education</option>
            <option value="Food">Food</option>
            <option value="Buissness">Buissness</option>
            <option value="Health">Health</option>
            <option value="Others">Others</option>
          </select>
        </div>

        <div class="input-group mb-3">
          <label class="input-group-text" for="inputGroupFile01">Upload</label>
          <input type="url" name="pic" class="form-control" id="inputGroupFile01">
        </div>
        <button type="submit" class="btn btn-outline-light">Post</button>
        </form>
        </div>
      `
      
    const cancel = document.querySelector(".X")
    cancel.addEventListener('click', function(){
        newpost.innerHTML=` `
    })
    })
    }
    
    //change profile
     const profileadd = document.querySelector(".profileadd")
    const changeprofile = document.querySelector(".changeprofile")

    if (profileadd && changeprofile) {
    profileadd.addEventListener('click', ()=>{
        changeprofile.innerHTML = `<div class="card text-center z-3 fixed-top mx-auto m-3 bg-secondary p-3"style="top: 3em; width: 80%; ">
        <div class="d-flex align-items-center justify-content-between p-1  m-0"> 
        <img class="rounded-circle border border-1 m-2" src="https://www.lights4fun.co.uk/cdn/shop/files/HA20003_3-Ghost-Garden-Stake-Lights.jpg?v=1742550678&width=1080" alt="" style="width: 3em;">
        <h5>Change your profile! </h5>
        <p><button class="X ">X</button></p>
        </div>
        <form action="/change" method="post">
        <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupSelect01">Cover picture</label>
        <input type="url" src="" name="cover" placholder="Url" class="form-control" id="inputGroupFile01">
        </div>

        <div class="input-group input-group-sm mb-3" >
        <label class="input-group-text" for="inputGroupSelect02">Profile Picture</label>
          <input type="url" name="profpic"  placholder="Url" class="form-control" id="inputGroupFile02">
        </div>

          <div class="input-group mb-3 " >
          <label class="input-group-text" for="inputGroupSelect03">Description</label>
          <input type="text" name="description"  placholder="description" class="form-control" id="inputGroupFile03">
          </div>

          <div class="input-group mb-3">
          <label class="input-group-text" for="inputGroupFile04">"You can contact me at:"</label>
          <input type="text" name="contact" placholder="Contact address" class="form-control" id="inputGroupFile04">
        </div>

        <div class="input-group mb-3">
          <label class="input-group-text" for="inputGroupFile05">About me</label>
          <input type="text" name="about" placholder="About me" class="form-control" id="inputGroupFile05">
        </div>
        <button type="submit" class="btn btn-outline-light">Submit</button>
        </form>
        </div>
      `
      
    const cancel = document.querySelector(".X")
    cancel.addEventListener('click', function(){
        changeprofile.innerHTML=` `
    })
    })
    } 

    
